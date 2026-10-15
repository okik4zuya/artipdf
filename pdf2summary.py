import json
import os
import re
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request

if sys.platform == "win32":
    import ctypes

# Explorer launches this exe in a console using the legacy system codepage
# (e.g. cp1252), which can't encode the arrows/checkmarks printed below and
# would otherwise crash with UnicodeEncodeError.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

DASHBOARD_URL = "http://127.0.0.1:4174/api/pdf-summarize"

# --- Multi-process coordination -------------------------------------------
#
# Same leader/follower pattern as pdf2md.py (see that file's comment for the
# full rationale) -- duplicated here with distinct mutex/temp-file names so a
# concurrent "Convert to Markdown" batch and a "Summarize with AI" batch never
# elect leaders or share manifests across each other.
IS_COORDINATED = getattr(sys, 'frozen', False) and sys.platform == "win32"

_LEADER_MUTEX_NAME = "Local\\ArtiPDFSummarize_Leader"
_QUEUE_LOCK_NAME = "Local\\ArtiPDFSummarize_QueueLock"
_ERROR_ALREADY_EXISTS = 183
_INFINITE = 0xFFFFFFFF

MANIFEST_PATH = os.path.join(tempfile.gettempdir(), "ArtiPDFSummarize_manifest.txt")
EVENTS_PATH = os.path.join(tempfile.gettempdir(), "ArtiPDFSummarize_events.txt")

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
    _queue_lock_acquire()
    try:
        for path in (MANIFEST_PATH, EVENTS_PATH):
            if not os.path.exists(path) or (time.time() - os.path.getmtime(path)) > 30:
                open(path, "w", encoding="utf-8").close()
    finally:
        _queue_lock_release()

    _register_files(_PDF_FILES)


# Election + registration happen immediately at import time, before the
# heavy pdfminer/pdf2image/pytesseract imports pulled in via pdf2md -- see
# pdf2md.py's block comment for why this ordering matters.
_PDF_FILES = sys.argv[1:]
_IS_LEADER = True
if IS_COORDINATED and _PDF_FILES:
    _IS_LEADER = _acquire_leadership()
    if _IS_LEADER:
        _run_leader()
    else:
        _run_follower()

from pdf2md import extract_raw_text  # noqa: E402


def _summarize_via_dashboard(text, filename):
    """POSTs extracted text to the ARTi dashboard's /api/pdf-summarize.
    Raises RuntimeError with a clear message on any failure -- no retry, no
    truncation, per the researcher's decision: a failed file is reported and
    the batch moves on."""
    payload = json.dumps({"text": text, "filename": filename}).encode("utf-8")
    req = urllib.request.Request(
        DASHBOARD_URL, data=payload, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise RuntimeError(
            "ARTi Dashboard is not running (could not reach http://127.0.0.1:4174). "
            "Start the dashboard and try again."
        ) from e
    except urllib.error.HTTPError as e:
        try:
            data = json.loads(e.read().decode("utf-8"))
            msg = data.get("error", str(e))
        except Exception:
            msg = str(e)
        raise RuntimeError(msg) from e
    if "error" in data:
        raise RuntimeError(data["error"])
    return data["summary"], data.get("model", "")


def _safe_model_slug(model_name):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", model_name).strip("-") or "model"


def summarize_one(pdf_path):
    """Extract + summarize one PDF. Returns (output_path, model_name, error)."""
    try:
        text = extract_raw_text(pdf_path)
        if not text.strip():
            return None, None, "No extractable text found in this PDF"
        summary, model_name = _summarize_via_dashboard(text, os.path.basename(pdf_path))
        output_path = (
            os.path.splitext(pdf_path)[0] + "_summary_" + _safe_model_slug(model_name) + ".md"
        )
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"# Summary: {os.path.basename(pdf_path)}\n\n" + summary)
        return output_path, model_name, None
    except Exception as e:
        return None, None, str(e)


def _convert_with_events(pdf_path):
    _write_event("START", pdf_path)
    if not os.path.exists(pdf_path):
        _write_event("FAIL", pdf_path, "File not found")
        return
    output_path, model_name, err = summarize_one(pdf_path)
    if err:
        _write_event("FAIL", pdf_path, err)
    else:
        _write_event("OK", pdf_path, output_path + "|" + (model_name or ""))


def _run_simple(pdf_files):
    """Unfrozen / non-Windows path: summarize files directly in one process."""
    total = len(pdf_files)

    print("\nPDF Summarize with AI")
    print("----------------------")

    for i, pdf in enumerate(pdf_files, start=1):
        if not os.path.exists(pdf):
            print(f"\n[{i}/{total}] Error: File not found: {pdf}")
            continue
        print(f"\n[{i}/{total}] Starting: {os.path.basename(pdf)}")
        output_path, model_name, err = summarize_one(pdf)
        if err:
            print(f"  Error: {err}")
        else:
            print(f"  Model: {model_name}")
            print(f"  Saved: {output_path}")

    print("\nDone.")


def _leader_convert_own():
    for pdf in _PDF_FILES:
        _convert_with_events(pdf)


def _run_leader_conversion():
    print("\nPDF Summarize with AI")
    print("----------------------")

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
                print(f"Summarizing: {name}")
            elif kind == "OK":
                completed += 1
                out_path, _, model_name = extra.partition("|")
                print(f"[{completed}/{total}] Saved: {os.path.basename(out_path)} (model: {model_name})")
            elif kind == "FAIL":
                completed += 1
                print(f"[{completed}/{total}] Error: {name} - {extra}")
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
        print("  python pdf2summary.py file1.pdf file2.pdf ...")
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
    if getattr(sys, 'frozen', False):
        input("\nPress Enter to close this window...")


if __name__ == "__main__":
    main()
