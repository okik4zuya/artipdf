import os
import shutil
import sys


def get_base_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    # app/ is one level inside the project root
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


IS_MAC = sys.platform == "darwin"

BASE_DIR = get_base_dir()

if IS_MAC:
    # Packaged builds bundle these under *-mac/ (see .github/workflows/release.yml).
    # Running from source on a real Mac, fall back to Homebrew-installed
    # binaries on PATH instead.
    _poppler_mac = os.path.join(BASE_DIR, "poppler-mac")
    POPPLER_PATH = _poppler_mac if os.path.isdir(_poppler_mac) else None

    _tesseract_mac = os.path.join(BASE_DIR, "tesseract-mac", "tesseract")
    TESSERACT_PATH = _tesseract_mac if os.path.isfile(_tesseract_mac) else (shutil.which("tesseract") or _tesseract_mac)

    _gs_mac = os.path.join(BASE_DIR, "ghostscript-mac", "gs")
    GHOSTSCRIPT_PATH = _gs_mac if os.path.isfile(_gs_mac) else (shutil.which("gs") or _gs_mac)
else:
    POPPLER_PATH     = os.path.join(BASE_DIR, "poppler", "Library", "bin")
    TESSERACT_PATH   = os.path.join(BASE_DIR, "tesseract", "tesseract.exe")
    GHOSTSCRIPT_PATH = os.path.join(BASE_DIR, "ghostscript", "bin", "gswin64c.exe")


def find_browser():
    """Locate a headless-capable Edge/Chrome install for MD -> PDF rendering."""
    if sys.platform == "win32":
        candidates = [
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Microsoft", "Edge", "Application", "msedge.exe"),
            os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft", "Edge", "Application", "msedge.exe"),
            os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("ProgramFiles", ""), "Google", "Chrome", "Application", "chrome.exe"),
        ]
    elif IS_MAC:
        candidates = [
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ]
    else:
        candidates = [shutil.which("msedge"), shutil.which("google-chrome"), shutil.which("chromium")]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None
