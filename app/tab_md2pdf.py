import os
import subprocess
import tempfile
import threading
import tkinter as tk
from tkinter import filedialog, ttk

import markdown

from .config import find_browser
from .widgets import DropZone, LogPanel

PAGE_SIZES = ("A4", "Letter", "Legal")
FONT_FAMILIES = ("Helvetica, sans-serif", "Georgia, serif", "Consolas, monospace")
LINE_SPACINGS = ("1", "1.15", "1.5", "2")
DEFAULT_FONT_SIZE = 12
DEFAULT_MARGIN_CM = 2
DEFAULT_LINE_SPACING = "1.15"


def _build_css(page_size: str, margin_cm: float, font_family: str, font_size: int,
               line_spacing: str) -> str:
    return f"""
<style>
@page {{ size: {page_size}; margin: {margin_cm}cm; }}
* {{ print-color-adjust: exact; -webkit-print-color-adjust: exact; }}
body {{ font-family: {font_family}; font-size: {font_size}pt; line-height: {line_spacing}; }}
p {{ margin: 0 0 {line_spacing}em 0; }}
h1, h2, h3, h4 {{ color: #1a1a1a; }}
code, pre {{ font-family: Consolas, monospace; background: #f0f0f0; }}
pre {{ padding: 6px; border: 1px solid #ddd; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ccc; padding: 4px 8px; }}
blockquote {{ color: #555; border-left: 3px solid #ccc; margin: 0; padding-left: 10px; }}
</style>
"""


def _md_to_pdf(md_text: str, out_path: str, page_size: str = "A4",
                margin_cm: float = DEFAULT_MARGIN_CM,
                font_family: str = FONT_FAMILIES[0],
                font_size: int = DEFAULT_FONT_SIZE,
                line_spacing: str = DEFAULT_LINE_SPACING):
    browser = find_browser()
    if not browser:
        raise RuntimeError("No headless-capable Edge/Chrome install found.")

    css = _build_css(page_size, margin_cm, font_family, font_size, line_spacing)
    html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    html = f"<html><head><meta charset=\"utf-8\">{css}</head><body>{html}</body></html>"

    fd, html_path = tempfile.mkstemp(suffix=".html")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(html)
        result = subprocess.run(
            [browser, "--headless", "--disable-gpu",
             f"--print-to-pdf={out_path}", "--print-to-pdf-no-header",
             "--no-pdf-header-footer", html_path],
            capture_output=True, text=True, timeout=60,
        )
        if not os.path.exists(out_path):
            raise RuntimeError(f"PDF generation failed: {result.stderr.strip()}")
    finally:
        os.remove(html_path)


class MdToPdfTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5f5f5")
        self.files: list[str] = []
        self.mode = tk.StringVar(value="files")
        self.page_size = tk.StringVar(value="A4")
        self.margin_cm = tk.StringVar(value=str(DEFAULT_MARGIN_CM))
        self.font_family = tk.StringVar(value=FONT_FAMILIES[0])
        self.font_size = tk.StringVar(value=str(DEFAULT_FONT_SIZE))
        self.line_spacing = tk.StringVar(value=DEFAULT_LINE_SPACING)
        self._build()

    def _build(self):
        mode_row = tk.Frame(self, bg="#f5f5f5")
        mode_row.pack(fill="x", padx=12, pady=(12, 4))
        tk.Label(mode_row, text="Input:", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(side="left")
        tk.Radiobutton(mode_row, text="Paste text", variable=self.mode,
                       value="paste", bg="#f5f5f5", font=("Segoe UI", 9),
                       command=self._switch_mode).pack(side="left", padx=6)
        tk.Radiobutton(mode_row, text="Select files", variable=self.mode,
                       value="files", bg="#f5f5f5", font=("Segoe UI", 9),
                       command=self._switch_mode).pack(side="left")

        # ── layout options ────────────────────────────────────────────
        layout_row = tk.Frame(self, bg="#f5f5f5")
        layout_row.pack(fill="x", padx=12, pady=(0, 4))

        tk.Label(layout_row, text="Page:", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(side="left")
        ttk.Combobox(layout_row, textvariable=self.page_size, values=PAGE_SIZES,
                     state="readonly", width=8).pack(side="left", padx=(4, 12))

        tk.Label(layout_row, text="Margin (cm):", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(side="left")
        tk.Spinbox(layout_row, textvariable=self.margin_cm, from_=0, to=10,
                   increment=0.5, width=5).pack(side="left", padx=(4, 12))

        tk.Label(layout_row, text="Font:", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(side="left")
        ttk.Combobox(layout_row, textvariable=self.font_family, values=FONT_FAMILIES,
                     state="readonly", width=18).pack(side="left", padx=(4, 12))

        tk.Label(layout_row, text="Size (pt):", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(side="left")
        tk.Spinbox(layout_row, textvariable=self.font_size, from_=6, to=36,
                   increment=1, width=4).pack(side="left", padx=(4, 12))

        tk.Label(layout_row, text="Spacing:", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(side="left")
        ttk.Combobox(layout_row, textvariable=self.line_spacing, values=LINE_SPACINGS,
                     state="readonly", width=5).pack(side="left", padx=(4, 0))

        # ── paste mode ─────────────────────────────────────────────
        self.paste_frame = tk.Frame(self, bg="#f5f5f5")
        text_wrap = tk.Frame(self.paste_frame, bg="#f5f5f5")
        text_wrap.pack(fill="both", expand=True)
        sb = tk.Scrollbar(text_wrap, orient="vertical")
        sb.pack(side="right", fill="y")
        self.text = tk.Text(text_wrap, font=("Consolas", 9), height=12,
                             wrap="word", yscrollcommand=sb.set,
                             relief="solid", bd=1)
        self.text.pack(fill="both", expand=True)
        sb.config(command=self.text.yview)

        paste_btn_row = tk.Frame(self.paste_frame, bg="#f5f5f5")
        paste_btn_row.pack(fill="x", pady=4)
        self.btn_paste = tk.Button(paste_btn_row, text="Convert to PDF", command=self._start,
                                    relief="flat", bg="#388e3c", fg="white",
                                    font=("Segoe UI", 9, "bold"), padx=14, pady=3,
                                    cursor="hand2")
        self.btn_paste.pack(side="right")

        # ── files mode ─────────────────────────────────────────────
        self.files_frame = tk.Frame(self, bg="#f5f5f5")
        DropZone(self.files_frame, label="Drop .md files here",
                 on_drop=self._add_files,
                 on_browse=self._browse).pack(fill="x", pady=(0, 4))

        list_frame = tk.Frame(self.files_frame, bg="#f5f5f5")
        list_frame.pack(fill="x", pady=4)
        tk.Label(list_frame, text="Files queued:", bg="#f5f5f5",
                 font=("Segoe UI", 9), fg="#333").pack(anchor="w")

        inner = tk.Frame(list_frame, bg="#f5f5f5")
        inner.pack(fill="x")
        lb_sb = tk.Scrollbar(inner, orient="vertical")
        lb_sb.pack(side="right", fill="y")
        self.listbox = tk.Listbox(inner, font=("Segoe UI", 9), height=4,
                                   yscrollcommand=lb_sb.set,
                                   bg="white", selectbackground="#bbdefb",
                                   relief="solid", bd=1)
        self.listbox.pack(fill="x", expand=True)
        lb_sb.config(command=self.listbox.yview)

        files_btn_row = tk.Frame(self.files_frame, bg="#f5f5f5")
        files_btn_row.pack(fill="x", pady=4)
        tk.Button(files_btn_row, text="Remove Selected", command=self._remove,
                  relief="flat", bg="#e0e0e0", padx=8, pady=3).pack(side="left")
        tk.Button(files_btn_row, text="Clear All", command=self._clear,
                  relief="flat", bg="#e0e0e0", padx=8, pady=3).pack(side="left", padx=6)
        self.btn_files = tk.Button(files_btn_row, text="Convert to PDF", command=self._start,
                                    relief="flat", bg="#388e3c", fg="white",
                                    font=("Segoe UI", 9, "bold"), padx=14, pady=3,
                                    cursor="hand2")
        self.btn_files.pack(side="right")

        self.files_frame.pack(fill="both", expand=True, padx=12, pady=4)
        self.btn = self.btn_files

        # ── log ─────────────────────────────────────────────────────
        self.log = LogPanel(self, height=7, bg="#f5f5f5")
        self.log.pack(fill="both", expand=True, padx=12, pady=(0, 12))

    # ── mode switching ───────────────────────────────────────────────

    def _switch_mode(self):
        if self.mode.get() == "paste":
            self.files_frame.pack_forget()
            self.paste_frame.pack(fill="both", expand=True, padx=12, pady=4,
                                   before=self.log)
            self.btn = self.btn_paste
        else:
            self.paste_frame.pack_forget()
            self.files_frame.pack(fill="both", expand=True, padx=12, pady=4,
                                   before=self.log)
            self.btn = self.btn_files

    # ── file management ─────────────────────────────────────────────

    def _browse(self):
        paths = filedialog.askopenfilenames(
            filetypes=[("Markdown files", "*.md;*.markdown")])
        self._add_files(list(paths))

    def _add_files(self, paths: list[str]):
        added = 0
        for p in paths:
            if p.lower().endswith((".md", ".markdown")) and p not in self.files:
                self.files.append(p)
                self.listbox.insert("end", os.path.basename(p))
                added += 1
        if added:
            self.log.write(f"Added {added} file(s).", "info")

    def _remove(self):
        sel = self.listbox.curselection()
        if sel:
            self.listbox.delete(sel[0])
            self.files.pop(sel[0])

    def _clear(self):
        self.listbox.delete(0, "end")
        self.files.clear()

    # ── conversion ──────────────────────────────────────────────────

    def _layout_kwargs(self):
        try:
            margin_cm = float(self.margin_cm.get())
        except ValueError:
            margin_cm = DEFAULT_MARGIN_CM
        try:
            font_size = int(float(self.font_size.get()))
        except ValueError:
            font_size = DEFAULT_FONT_SIZE
        return {
            "page_size": self.page_size.get(),
            "margin_cm": margin_cm,
            "font_family": self.font_family.get(),
            "font_size": font_size,
            "line_spacing": self.line_spacing.get(),
        }

    def _start(self):
        layout = self._layout_kwargs()
        if self.mode.get() == "paste":
            text = self.text.get("1.0", "end").strip()
            if not text:
                self.log.write("No Markdown text to convert.", "err")
                return
            out_path = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if not out_path:
                return
            self.btn.configure(state="disabled", text="Converting…")
            threading.Thread(target=self._run_paste, args=(text, out_path, layout),
                              daemon=True).start()
        else:
            if not self.files:
                self.log.write("No files queued.", "err")
                return
            self.btn.configure(state="disabled", text="Converting…")
            threading.Thread(target=self._run_files, args=(list(self.files), layout),
                              daemon=True).start()

    def _run_paste(self, text: str, out_path: str, layout: dict):
        try:
            _md_to_pdf(text, out_path, **layout)
            self.after(0, lambda: self.log.write_link("✔ Saved: ", out_path, "ok"))
        except Exception as e:
            self.after(0, lambda e=e: self.log.write(f"✘ Error: {e}", "err"))
        finally:
            self.after(0, lambda: self.btn.configure(state="normal", text="Convert to PDF"))

    def _run_files(self, files: list[str], layout: dict):
        for i, path in enumerate(files, 1):
            self.after(0, lambda p=path, n=i, t=len(files):
                       self.log.write(f"\n[{n}/{t}] {os.path.basename(p)}", "info"))
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                out_path = os.path.splitext(path)[0] + ".pdf"
                _md_to_pdf(text, out_path, **layout)
                self.after(0, lambda p=out_path: self.log.write_link("  ✔ Saved: ", p, "ok"))
            except Exception as e:
                self.after(0, lambda e=e: self.log.write(f"  ✘ Error: {e}", "err"))
        self.after(0, lambda: self.log.write("\nAll done.", "ok"))
        self.after(0, lambda: self.btn.configure(state="normal", text="Convert to PDF"))
