# Third-party notices

ARTi PDF's own code is MIT-licensed (see [LICENSE](LICENSE)). The installer and portable build
also ship the programs and libraries below, each under its own license. They are separate works:
ARTi PDF starts Ghostscript, Poppler and Tesseract as separate programs (subprocess calls) and does
not link against them.

## Bundled programs

| Component | Version | License | Used for | Source |
| --- | --- | --- | --- | --- |
| Ghostscript | 10.07.0 | AGPL-3.0 | Compress | <https://ghostscript.com/releases/> |
| Poppler (Windows build) | 25.07.0 | GPL-2.0-or-later, plus the licenses of the DLLs shipped in the same build | Rendering pages for OCR and thumbnails | <https://poppler.freedesktop.org/> and <https://github.com/oschwartz10612/poppler-windows> |
| Tesseract OCR | 5.5.0 | Apache-2.0 | OCR for scanned PDFs | <https://github.com/tesseract-ocr/tesseract> |
| Leptonica (inside Tesseract) | 1.85.0 | BSD-2-Clause | Image handling for OCR | <https://github.com/DanBloomberg/leptonica> |
| `eng.traineddata` | tessdata release | Apache-2.0 | English OCR model | <https://github.com/tesseract-ocr/tessdata> |

The corresponding source of each bundled program is available at the links above. If you cannot
obtain it there, open an issue at <https://github.com/okik4zuya/artipdf> and it will be provided.

## Python packages

| Package | Version | License |
| --- | --- | --- |
| pdfminer.six | 20250506 | MIT |
| pdf2image | 1.17.0 | MIT |
| Pillow | 11.3.0 | MIT-CMU (HPND) |
| pytesseract | 0.3.13 | Apache-2.0 |
| pypdf | 6.10.1 | BSD-3-Clause |
| tkinterdnd2 | 0.4.2 | MIT |
| Markdown | 3.10.3 | BSD-3-Clause |
| PyInstaller (build tool, bootloader is included in the exe) | 6.14.0 | GPL-2.0-or-later with a special exception that permits bundling non-GPL programs |

## Not bundled

MD to PDF uses the Microsoft Edge or Google Chrome already installed on your computer (headless
print). They are not shipped with ARTi PDF and are covered by their own terms.

Versions above are the ones in `requirements.txt` and the bundled binaries at the time of writing;
update this file when a component is upgraded.
