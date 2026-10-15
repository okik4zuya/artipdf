"""GUI-free PDF compression, shared by the Compress tab and ArtiPDFCompress.exe."""
import io
import os
import shutil
import subprocess
import sys

import PIL.Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, NameObject, NumberObject

from .config import GHOSTSCRIPT_PATH


def _find_ghostscript() -> str | None:
    """Return path to gswin64c.exe — bundled first, then system PATH."""
    if os.path.isfile(GHOSTSCRIPT_PATH):
        return GHOSTSCRIPT_PATH
    for exe in ("gswin64c", "gswin32c", "gs"):
        path = shutil.which(exe)
        if path:
            return path
    return None


_GS_SETTINGS = {
    "low":    "/screen",
    "medium": "/ebook",
    "high":   "/printer",
    "custom": "/ebook",
}


_PRESETS = {
    "low":    dict(quality=40,  dpi=96,  meta=True,  streams=True, thumbs=False),
    "medium": dict(quality=65,  dpi=150, meta=True,  streams=True, thumbs=False),
    "high":   dict(quality=85,  dpi=300, meta=False, streams=True, thumbs=False),
}


def _human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} GB"


def _compress_xobject_dict(xobjects, quality: int, max_px: float | None) -> int:
    """Re-compress raster images in an XObject dict. Returns count replaced."""
    count = 0
    for key in list(xobjects.keys()):
        try:
            xobj = xobjects[key].get_object()
            subtype = xobj.get("/Subtype")

            # Recurse into Form XObjects — they carry their own Resources/XObject tree
            if subtype == "/Form":
                form_res = xobj.get("/Resources")
                if form_res:
                    form_res = form_res.get_object()
                    form_xobjs = form_res.get("/XObject")
                    if form_xobjs:
                        count += _compress_xobject_dict(
                            form_xobjs.get_object(), quality, max_px
                        )
                continue

            if subtype != "/Image":
                continue

            # Skip colour-key / stencil hard masks (rare, complex)
            if "/Mask" in xobj and "/SMask" not in xobj:
                continue

            width  = int(xobj["/Width"])
            height = int(xobj["/Height"])
            bits   = int(xobj.get("/BitsPerComponent", 8))
            if bits != 8:
                continue

            cs_obj = xobj.get("/ColorSpace")
            if cs_obj is None:
                continue
            cs_res  = cs_obj.get_object() if hasattr(cs_obj, "get_object") else cs_obj
            cs_name = str(cs_res[0] if isinstance(cs_res, ArrayObject) else cs_res)

            if   "Gray" in cs_name: mode, ch = "L",    1
            elif "CMYK" in cs_name: mode, ch = "CMYK", 4
            elif "RGB"  in cs_name: mode, ch = "RGB",  3
            else:                   continue

            filt_obj = xobj.get("/Filter")
            is_jpeg  = filt_obj is not None and "DCTDecode" in str(filt_obj)
            raw      = xobj.get_data()

            if is_jpeg:
                img = PIL.Image.open(io.BytesIO(raw))
                img.load()
            else:
                if len(raw) != width * height * ch:
                    continue
                img = PIL.Image.frombytes(mode, (width, height), raw)

            # Composite SMask (soft alpha) onto white so the output is opaque JPEG
            smask_handled = False
            smask_ref = xobj.get("/SMask")
            if smask_ref is not None:
                try:
                    smask_obj = smask_ref.get_object()
                    sw = int(smask_obj["/Width"])
                    sh = int(smask_obj["/Height"])
                    mask_raw = smask_obj.get_data()
                    if len(mask_raw) == sw * sh:
                        alpha = PIL.Image.frombytes("L", (sw, sh), mask_raw)
                        rgba  = img.convert("RGBA")
                        rgba.putalpha(
                            alpha.resize((img.width, img.height), PIL.Image.LANCZOS)
                        )
                        background = PIL.Image.new("RGB", rgba.size, (255, 255, 255))
                        background.paste(rgba, mask=rgba.split()[3])
                        img = background
                        smask_handled = True
                except Exception:
                    pass

            # Downsample if longest axis exceeds the DPI target for this page
            if max_px and max(img.width, img.height) > max_px:
                ratio = max_px / max(img.width, img.height)
                img   = img.resize(
                    (max(1, int(img.width * ratio)), max(1, int(img.height * ratio))),
                    PIL.Image.LANCZOS,
                )

            out_img = img.convert("RGB") if mode == "CMYK" else img
            buf = io.BytesIO()
            out_img.save(buf, "JPEG", quality=quality, optimize=True)
            compressed = buf.getvalue()

            if len(compressed) >= len(raw):
                continue

            for k in ("/Filter", "/DecodeParms"):
                if k in xobj:
                    del xobj[k]
            xobj.set_data(compressed)
            xobj[NameObject("/Filter")]           = NameObject("/DCTDecode")
            xobj[NameObject("/Width")]            = NumberObject(out_img.width)
            xobj[NameObject("/Height")]           = NumberObject(out_img.height)
            xobj[NameObject("/BitsPerComponent")] = NumberObject(8)
            if mode == "CMYK":
                xobj[NameObject("/ColorSpace")] = NameObject("/DeviceRGB")
            if smask_handled and "/SMask" in xobj:
                del xobj["/SMask"]
            count += 1

        except Exception:
            continue

    return count


def _compress_images_on_page(page, quality: int, max_dpi: int | None) -> int:
    """Re-compress raster images on a page using Pillow. Returns count replaced."""
    resources = page.get("/Resources")
    if not resources:
        return 0
    resources = resources.get_object()
    xobjects = resources.get("/XObject")
    if not xobjects:
        return 0

    if max_dpi:
        try:
            mb = page.mediabox
            max_px = max(float(mb.width), float(mb.height)) / 72.0 * max_dpi
        except Exception:
            max_px = float(max_dpi * 11)
    else:
        max_px = None

    return _compress_xobject_dict(xobjects.get_object(), quality, max_px)


def default_opts(preset: str = "medium") -> dict:
    p = _PRESETS.get(preset, _PRESETS["medium"])
    return {
        "preset":           preset,
        "img_quality":      p["quality"],
        "max_dpi":          p["dpi"],
        "remove_meta":      p["meta"],
        "compress_streams": p["streams"],
        "remove_images":    p["thumbs"],
    }


def compress_pdf(path: str, out_path: str, opts: dict, log=lambda msg: None) -> tuple[int, int]:
    """Compress `path` into `out_path`. Returns (size_before, size_after) in bytes."""
    before = os.path.getsize(path)

    gs = _find_ghostscript()
    if gs:
        log("  Using GhostScript…")
        gs_setting = _GS_SETTINGS.get(opts.get("preset", "medium"), "/ebook")

        env = os.environ.copy()
        if sys.platform == "darwin":
            # Bundled macOS gs binary has no compiled-in prefix, so it
            # can't find its own init/font files unless GS_LIB points
            # at the Resource/lib dirs staged alongside it in CI.
            gs_dir = os.path.dirname(gs)
            resource_dir = os.path.join(gs_dir, "Resource")
            lib_dir = os.path.join(gs_dir, "lib")
            gs_lib_dirs = [d for d in (resource_dir, lib_dir) if os.path.isdir(d)]
            if gs_lib_dirs:
                env["GS_LIB"] = os.pathsep.join(gs_lib_dirs)

        subprocess.run(
            [
                gs,
                "-dNOPAUSE", "-dBATCH", "-dQUIET",
                "-sDEVICE=pdfwrite",
                "-dCompatibilityLevel=1.4",
                f"-dPDFSETTINGS={gs_setting}",
                f"-sOutputFile={out_path}",
                path,
            ],
            check=True,
            env=env,
            # CREATE_NO_WINDOW is Windows-only; subprocess raises
            # ValueError if creationflags is nonzero on POSIX.
            creationflags=0x08000000 if sys.platform == "win32" else 0,
        )
    else:
        log("  GhostScript not found — using pypdf fallback.")
        reader  = PdfReader(path)
        writer  = PdfWriter()
        quality = opts["img_quality"]
        max_dpi = opts["max_dpi"]

        for page in reader.pages:
            new_page = writer.add_page(page)
            if opts["compress_streams"]:
                new_page.compress_content_streams()
            if quality < 95 or max_dpi:
                _compress_images_on_page(new_page, quality, max_dpi)

        if not opts["remove_meta"] and reader.metadata:
            writer.add_metadata(reader.metadata)

        writer.compress_identical_objects()

        if opts["remove_images"]:
            for page in writer.pages:
                if "/Resources" in page and "/XObject" in page["/Resources"]:
                    del page["/Resources"]["/XObject"]

        with open(out_path, "wb") as f:
            writer.write(f)

    return before, os.path.getsize(out_path)
