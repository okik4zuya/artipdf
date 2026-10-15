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

# One-click context menu: fixed preset, same default as the Compress tab.
PRESET = "medium"

# --- Multi-process coordination -------------------------------------------
#
# Same leader/follower pattern as pdf2md.py (see that file's comment for the
# full rationale) -- duplicated here with distinct mutex/temp-file names so
# concurrent Convert / Summarize / Compress batches never elect leaders or
# share manifests across each other.
IS_COORDINATED = getattr(sys, 'frozen', False) and sys.platform == "win32"

_LEADER_MUTEX_NAME = "Local\\ArtiPDFCompress_Leader"
_QUEUE_LOCK_NAME = "Local\\ArtiPDFCompress_QueueLock"
_ERROR_ALREADY_EXISTS = 183
_INFINITE = 0xFFFFFFFF

MANIFEST_PATH = os.path.join(tempfile.gettempdir(), "ArtiPDFCompress_manifest.txt")
EVENTS_PATH = os.path.join(tempfile.gettempdir(), "ArtiPDFCompress_events.txt")

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
# heavy pypdf/Pillow imports pulled in via app.compress_core -- see
# pdf2md.py's block comment for why this ordering matters.
_PDF_FILES = sys.argv[1:]
_IS_LEADER = True
if IS_COORDINATED and _PDF_FILES:
    _IS_LEADER = _acquire_leadership()
    if _IS_LEADER:
        _run_leader()
    else:
        _run_follower()

from app.compress_core import compress_pdf, default_opts, _human_size  # noqa: E402


def _output_path(pdf_path):
    """<stem>_compressed.pdf next to the source; never overwrites an existing file."""
    stem = os.path.splitext(pdf_path)[0]
    out = stem + "_compressed.pdf"
    n = 2
    while os.path.exists(out):
        out = f"{stem}_compressed_{n}.pdf"
        n += 1
    return out


def compress_one(pdf_path):
    """Compress one PDF. Returns (output_path, before, after, error)."""
    try:
        out_path = _output_path(pdf_path)
        before, after = compress_pdf(pdf_path, out_path, default_opts(PRESET))
        return out_path, before, after, None
    except Exception as e:
        return None, 0, 0, str(e)


def _size_summary(before, after):
    pct = (before - after) / before * 100 if before else 0
    if after < before:
        return f"{_human_size(before)} -> {_human_size(after)} (-{pct:.1f}%)"
    return f"{_human_size(before)} -> {_human_size(after)} (no size reduction)"


def _compress_with_events(pdf_path):
    _write_event("START", pdf_path)
    if not os.path.exists(pdf_path):
        _write_event("FAIL", pdf_path, "File not found")
        return
    out_path, before, after, err = compress_one(pdf_path)
    if err:
        _write_event("FAIL", pdf_path, err)
    else:
        _write_event("OK", pdf_path, f"{out_path}|{_size_summary(before, after)}")


def _run_simple(pdf_files):
    """Unfrozen / non-Windows path: compress files directly in one process."""
    total = len(pdf_files)

    print("\nPDF Compress")
    print("-------------")

    for i, pdf in enumerate(pdf_files, start=1):
        if not os.path.exists(pdf):
            print(f"\n[{i}/{total}] Error: File not found: {pdf}")
            continue
        print(f"\n[{i}/{total}] Starting: {os.path.basename(pdf)}")
        out_path, before, after, err = compress_one(pdf)
        if err:
            print(f"  Error: {err}")
        else:
            print(f"  Saved: {out_path}")
            print(f"  {_size_summary(before, after)}")

    print("\nDone.")


def _leader_convert_own():
    for pdf in _PDF_FILES:
        _compress_with_events(pdf)


def _run_leader_conversion():
    print("\nPDF Compress")
    print("-------------")

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
                print(f"Compressing: {name}")
            elif kind == "OK":
                completed += 1
                out_path, _, summary = extra.partition("|")
                print(f"[{completed}/{total}] Saved: {os.path.basename(out_path)}  {summary}")
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
        _compress_with_events(pdf)


def main():
    if not _PDF_FILES:
        print("Usage:")
        print("  python pdf2compress.py file1.pdf file2.pdf ...")
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
