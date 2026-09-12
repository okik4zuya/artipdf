@echo off
setlocal

set "SCRIPT_DIR=%~dp0"

REM ── Run the existing PyInstaller build first ──────────────────────────
REM Suppress build.bat's own "pause" so it returns control here automatically
REM instead of stalling on a keypress before the installer step ever runs.
set "CI=1"
call "%SCRIPT_DIR%build.bat"

if not exist "%SCRIPT_DIR%dist\ArtiPDF\ArtiPDF.exe" (
    echo.
    echo Build failed — skipping installer step.
    exit /b 1
)

REM ── Locate makensis ────────────────────────────────────────────────────
where makensis >nul 2>nul
if errorlevel 1 (
    echo.
    echo ERROR: makensis not found on PATH.
    echo Install NSIS from https://nsis.sourceforge.io/Download and ensure
    echo its install directory ^(containing makensis.exe^) is on PATH.
    exit /b 1
)

echo.
echo Building installer...
echo.

makensis "%SCRIPT_DIR%installer.nsi"

echo.
echo Done. Setup exe is in %SCRIPT_DIR%dist\
pause
