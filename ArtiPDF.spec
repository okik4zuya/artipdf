# -*- mode: python ; coding: utf-8 -*-

# Four entry points share one onedir bundle (via MERGE) so all four land in
# dist\ArtiPDF\ without duplicating poppler/tesseract/ghostscript/app resources:
#   ArtiPDF.exe          — windowed GUI (pdf2md_gui.py)
#   ArtiPDFConvert.exe   — console CLI used by the Explorer "Convert to
#                          Markdown" context menu (pdf2md.py), so bulk/
#                          multi-select conversions have a visible progress
#                          window instead of running behind the GUI.
#   ArtiPDFSummarize.exe — console CLI used by the Explorer "Summarize with
#                          AI" context menu (pdf2summary.py); extracts text
#                          the same way as ArtiPDFConvert but posts it to the
#                          ARTi dashboard's /api/pdf-summarize instead of
#                          writing a local Markdown conversion.
#   ArtiPDFCompress.exe  — console CLI used by the Explorer "Compress PDF"
#                          context menu (pdf2compress.py); shares
#                          app/compress_core.py with the GUI Compress tab.

a_gui = Analysis(
    ['pdf2md_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('poppler', 'poppler'), ('tesseract', 'tesseract'), ('app', 'app'), ('ghostscript', 'ghostscript'), ('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

a_cli = Analysis(
    ['pdf2md.py'],
    pathex=[],
    binaries=[],
    datas=[('poppler', 'poppler'), ('tesseract', 'tesseract'), ('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

a_summary = Analysis(
    ['pdf2summary.py'],
    pathex=[],
    binaries=[],
    datas=[('poppler', 'poppler'), ('tesseract', 'tesseract'), ('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

a_compress = Analysis(
    ['pdf2compress.py'],
    pathex=[],
    binaries=[],
    datas=[('ghostscript', 'ghostscript'), ('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

MERGE(
    (a_gui, 'pdf2md_gui', 'ArtiPDF'),
    (a_cli, 'pdf2md', 'ArtiPDFConvert'),
    (a_summary, 'pdf2summary', 'ArtiPDFSummarize'),
    (a_compress, 'pdf2compress', 'ArtiPDFCompress'),
)

pyz_gui = PYZ(a_gui.pure)

exe_gui = EXE(
    pyz_gui,
    a_gui.scripts,
    [],
    exclude_binaries=True,
    name='ArtiPDF',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)

pyz_cli = PYZ(a_cli.pure)

exe_cli = EXE(
    pyz_cli,
    a_cli.scripts,
    [],
    exclude_binaries=True,
    name='ArtiPDFConvert',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)

pyz_summary = PYZ(a_summary.pure)

exe_summary = EXE(
    pyz_summary,
    a_summary.scripts,
    [],
    exclude_binaries=True,
    name='ArtiPDFSummarize',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)

pyz_compress = PYZ(a_compress.pure)

exe_compress = EXE(
    pyz_compress,
    a_compress.scripts,
    [],
    exclude_binaries=True,
    name='ArtiPDFCompress',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)

coll = COLLECT(
    exe_gui,
    a_gui.binaries,
    a_gui.datas,
    exe_cli,
    a_cli.binaries,
    a_cli.datas,
    exe_summary,
    a_summary.binaries,
    a_summary.datas,
    exe_compress,
    a_compress.binaries,
    a_compress.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ArtiPDF',
)
