import os
import sys
import tempfile
import threading
import time

if sys.platform == "win32":
    import ctypes

# Explorer launches this exe in a console using the legacy system codepage
# (e.g. cp1252), which can't encode the arrows/checkmarks printed below and
# would otherwise crash with UnicodeEncodeError.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

# --- Multi-process coordination -------------------------------------------
#
# When Explorer launches "Convert to Markdown" on several selected PDFs, it
# starts one process per file (see installer.nsi). To avoid one console
# window per file, the frozen exe elects a single "leader" process (via a
# named mutex) that owns the one visible console; every other ("follower")
# process hides its own console, converts its file(s) silently, and reports
# progress to the leader through two shared temp files.
#
# This whole block runs BEFORE the heavy pdfminer/pdf2image/pytesseract
# imports below, and a follower hides its console as its very first action,
# because those imports can take a second or more per process when many
# processes start at once (14 files = 14 concurrent cold imports) - if the
# election/hide happened after the imports, every follower's console would
# sit visible for that whole import duration before disappearing.
IS_COORDINATED = getattr(sys, 'frozen', False) and sys.platform == "win32"

# Local\ (not Global\) namespace: Explorer and every process it spawns for
# this batch run in the same interactive session, and creating a "Global\"
# named object requires SeCreateGlobalPrivilege, which ordinary user
# processes don't have - CreateMutexW would fail with ERROR_ACCESS_DENIED
# (not ERROR_ALREADY_EXISTS), making every process think it's the leader.
_LEADER_MUTEX_NAME = "Local\\ArtiPDFConvert_Leader"
_QUEUE_LOCK_NAME = "Local\\ArtiPDFConvert_QueueLock"
_ERROR_ALREADY_EXISTS = 183
_INFINITE = 0xFFFFFFFF

MANIFEST_PATH = os.path.join(tempfile.gettempdir(), "ArtiPDFConvert_manifest.txt")
EVENTS_PATH = os.path.join(tempfile.gettempdir(), "ArtiPDFConvert_events.txt")

_leader_mutex_handle = None
_queue_lock_handle = None

if sys.platform == "win32":
    from ctypes import wintypes
    _kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _kernel32.CreateMutexW.restype = wintypes.HANDLE
    _kernel32.CreateMutexW.argtypes = (wintypes.LPCVOID, wintypes.BOOL, wintypes.LPCWSTR)
    _kernel32.WaitForSingleObject.restype = wintypes.DWORD
    _kernel32.WaitForSingleObject.argtypes = (wintypes.HANDLE, wintypes.DWORD)
    _kernel32.ReleaseMutex.argtypes = (wintypes.HANDLE,)
    _kernel32.GetConsoleWindow.restype = wintypes.HWND


def _queue_lock_acquire():
    _kernel32.WaitForSingleObject(_queue_lock_handle, _INFINITE)


def _queue_lock_release():
    _kernel32.ReleaseMutex(_queue_lock_handle)


def _acquire_leadership():
    """Return True if this process is the leader for the current batch.

    Falls back to True (uncoordinated/standalone) if the mutex can't be
    created at all, so a permission failure never leaves a file silently
    unconverted - it just loses console coalescing for that run.
    """
    global _leader_mutex_handle, _queue_lock_handle
    ctypes.set_last_error(0)
    _leader_mutex_handle = _kernel32.CreateMutexW(None, False, _LEADER_MUTEX_NAME)
    err = ctypes.get_last_error()
    if not _leader_mutex_handle:
        return True
    is_leader = err != _ERROR_ALREADY_EXISTS
    _queue_lock_handle = _kernel32.CreateMutexW(None, False, _QUEUE_LOCK_NAME)
    if not _queue_lock_handle:
        return True
    return is_leader


def _hide_console():
    hwnd = _kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # SW_HIDE


def _register_files(paths):
    """Append this process's file paths to the shared manifest."""
    _queue_lock_acquire()
    try:
        with open(MANIFEST_PATH, "a", encoding="utf-8") as f:
            for p in paths:
                f.write(p + "\n")
    finally:
        _queue_lock_release()


def _write_event(kind, path, extra=""):
    _queue_lock_acquire()
    try:
        with open(EVENTS_PATH, "a", encoding="utf-8") as f:
            f.write(f"{kind}\t{path}\t{extra}\n")
    finally:
        _queue_lock_release()


def _read_new_events(offset):
    """Read events appended since `offset`. Returns (new_offset, [(kind, path, extra), ...])."""
    _queue_lock_acquire()
    try:
        with open(EVENTS_PATH, "r", encoding="utf-8") as f:
            f.seek(offset)
            new_data = f.read()
            new_offset = f.tell()
    finally:
        _queue_lock_release()

    events = []
    for line in new_data.splitlines():
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) == 2:
            parts.append("")
        events.append(tuple(parts[:3]))
    return new_offset, events


def _discover_total():
    """Debounce-poll the manifest until its line count settles, to learn the batch size."""
    deadline = time.time() + 8.0
    last_count = -1
    stable_since = None
    while time.time() < deadline:
        _queue_lock_acquire()
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                count = sum(1 for _ in f)
        finally:
            _queue_lock_release()

        if count == last_count:
            if stable_since is None:
                stable_since = time.time()
            elif time.time() - stable_since >= 0.5:
                return count
        else:
            stable_since = None
            last_count = count
        time.sleep(0.1)
    return max(last_count, 1)


def _run_follower():
    _hide_console()
    _register_files(_PDF_FILES)


def _run_leader():
    # Fresh-create the shared temp files for this batch, unless a follower
    # that started microseconds earlier has already registered into them
    # (in which case truncating would drop that follower's entry) - only
    # reset files that are stale leftovers from a crashed previous run.
    _queue_lock_acquire()
    try:
        for path in (MANIFEST_PATH, EVENTS_PATH):
            if not os.path.exists(path) or (time.time() - os.path.getmtime(path)) > 30:
                open(path, "w", encoding="utf-8").close()
    finally:
        _queue_lock_release()

    _register_files(_PDF_FILES)


# Election + registration happen immediately at import time, before the
# heavy pdfminer/pdf2image/pytesseract imports below - see block comment
# above. `main()` (called after those imports finish) uses the results.
_PDF_FILES = sys.argv[1:]
_IS_LEADER = True
if IS_COORDINATED and _PDF_FILES:
    _IS_LEADER = _acquire_leadership()
    if _IS_LEADER:
        _run_leader()
    else:
        _run_follower()

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from pdf2image import convert_from_path
import pytesseract


def get_base_dir():
    """Return base directory (handles PyInstaller _MEIPASS)."""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


IS_MAC = sys.platform == "darwin"
BASE_DIR = get_base_dir()

if IS_MAC:
    POPPLER_PATH = os.path.join(BASE_DIR, "poppler-mac")
    TESSERACT_PATH = os.path.join(BASE_DIR, "tesseract-mac", "tesseract")
else:
    POPPLER_PATH = os.path.join(BASE_DIR, "poppler", "Library", "bin")
    TESSERACT_PATH = os.path.join(BASE_DIR, "tesseract", "tesseract.exe")

if os.path.exists(TESSERACT_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# In coordinated runs, extract_text_to_markdown()'s own per-step prints are
# redundant (the leader already reports START/OK/FAIL for every file via the
# events feed) and, for the leader's own file, would print a second time
# straight to the shared console alongside the event-driven lines. Route
# them through _log so they're silent whenever a run is coordinated,
# regardless of whether this particular process is the leader or a
# (invisible) follower.
if IS_COORDINATED:
    def _log(*_args, **_kwargs):
        pass
else:
    _log = print


def extract_raw_text(pdf_path):
    """Extract a PDF's text (pdfminer, falling back to full or per-page OCR).
    Returns plain text only -- no Markdown framing, no file written. Shared by
    extract_text_to_markdown() below and pdf2summary.py's AI-summarize path."""
    _log(f"\nProcessing: {os.path.basename(pdf_path)}")

    # Step 1: Try normal extraction, per page
    page_texts = []
    for layout in extract_pages(pdf_path):
        page_text = "".join(
            el.get_text() for el in layout
            if isinstance(el, LTTextContainer)
        )
        page_texts.append(page_text)

    text = "\n".join(page_texts)

    if not text.strip():
        _log("  No text detected → running OCR...")

        pages = convert_from_path(
            pdf_path,
            dpi=300,
            poppler_path=POPPLER_PATH
        )

        text_list = []

        for i, page in enumerate(pages, start=1):
            _log(f"  OCR page {i}/{len(pages)}...")
            ocr_text = pytesseract.image_to_string(page)
            text_list.append(ocr_text)

        text = "\n".join(text_list)

    else:
        broken = [i for i, pt in enumerate(page_texts) if "�" in pt]
        if broken:
            _log(f"  Broken glyphs on page(s) {', '.join(str(i + 1) for i in broken)} "
                 "→ running OCR for those...")
            for i in broken:
                ocr_pages = convert_from_path(
                    pdf_path, dpi=300, poppler_path=POPPLER_PATH,
                    first_page=i + 1, last_page=i + 1
                )
                page_texts[i] = pytesseract.image_to_string(ocr_pages[0])
            text = "\n".join(page_texts)
        _log("  Text layer detected.")

    return text


def extract_text_to_markdown(pdf_path):
    """Convert one PDF file to Markdown. Returns (output_path, error)."""
    try:
        output_md = os.path.splitext(pdf_path)[0] + ".md"
        text = extract_raw_text(pdf_path)
        md_content = "# Extracted PDF Content\n\n" + text

        with open(output_md, "w", encoding="utf-8") as f:
            f.write(md_content)

        _log(f"  ✔ Saved: {output_md}")
        return output_md, None

    except Exception as e:
        _log(f"  ❌ Error processing {pdf_path}")
        _log(f"     {e}")
        return None, str(e)


def _convert_with_events(pdf_path):
    """Convert one file, reporting START/OK/FAIL through the shared events file."""
    _write_event("START", pdf_path)
    if not os.path.exists(pdf_path):
        _write_event("FAIL", pdf_path, "File not found")
        return
    output_md, err = extract_text_to_markdown(pdf_path)
    if err:
        _write_event("FAIL", pdf_path, err)
    else:
        _write_event("OK", pdf_path, output_md)


def _run_simple(pdf_files):
    """Unfrozen / non-Windows path: convert files directly in one process."""
    total = len(pdf_files)

    print("\nPDF → Markdown Conversion")
    print("-------------------------")

    for i, pdf in enumerate(pdf_files, start=1):

        if not os.path.exists(pdf):
            print(f"\n[{i}/{total}] ❌ File not found: {pdf}")
            continue

        print(f"\n[{i}/{total}] Starting...")
        extract_text_to_markdown(pdf)

    print("\nDone.")


def _leader_convert_own():
    for pdf in _PDF_FILES:
        _convert_with_events(pdf)


def _run_leader_conversion():
    """Own the visible console: kick off this process's own file(s) in the
    background, then tail the shared events file and print unified
    per-file progress for the whole batch until every registered file has
    reported completion."""
    print("\nPDF → Markdown Conversion")
    print("-------------------------")

    worker = threading.Thread(target=_leader_convert_own, daemon=True)
    worker.start()

    total = _discover_total()

    offset = 0
    completed = 0
    while completed < total:
        offset, events = _read_new_events(offset)
        for kind, path, extra in events:
            name = os.path.basename(path)
            if kind == "START":
                print(f"Processing: {name}")
            elif kind == "OK":
                completed += 1
                print(f"[{completed}/{total}] ✔ Saved: {os.path.basename(extra)}")
            elif kind == "FAIL":
                completed += 1
                print(f"[{completed}/{total}] ❌ Error: {name} - {extra}")
        if completed < total:
            time.sleep(0.1)

    worker.join()
    print("\nDone.")

    for p in (MANIFEST_PATH, EVENTS_PATH):
        try:
            os.remove(p)
        except OSError:
            pass


def _run_follower_conversion():
    for pdf in _PDF_FILES:
        _convert_with_events(pdf)


def main():

    if not _PDF_FILES:
        print("Usage:")
        print("  python pdf_to_md.py file1.pdf file2.pdf ...")
        _pause_if_frozen()
        sys.exit(1)

    if not IS_COORDINATED:
        _run_simple(_PDF_FILES)
        _pause_if_frozen()
        return

    if _IS_LEADER:
        _run_leader_conversion()
        _pause_if_frozen()
    else:
        _run_follower_conversion()


def _pause_if_frozen():
    """Keep the console window open when launched from Explorer (frozen exe)."""
    if getattr(sys, 'frozen', False):
        input("\nPress Enter to close this window...")


if __name__ == "__main__":
    main()
