import os
import threading
import tkinter as tk
from tkinter import filedialog

from .compress_core import _PRESETS, _human_size, compress_pdf
from .widgets import DropZone, LogPanel

class CompressTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#f5f5f5")
        self.files: list[str] = []
        self._build()

    def _build(self):
        BG = "#f5f5f5"

        DropZone(self, label="Drop PDF files here",
                 on_drop=self._add_files,
                 on_browse=self._browse).pack(fill="x", padx=12, pady=(12, 4))

        # File list — fixed height, no expand
        list_frame = tk.Frame(self, bg=BG)
        list_frame.pack(fill="x", padx=12, pady=(0, 4))
        tk.Label(list_frame, text="Files queued:", bg=BG,
                 font=("Segoe UI", 9), fg="#333").pack(anchor="w")
        inner = tk.Frame(list_frame, bg=BG)
        inner.pack(fill="x")
        sb = tk.Scrollbar(inner, orient="vertical")
        sb.pack(side="right", fill="y")
        self.listbox = tk.Listbox(inner, font=("Segoe UI", 9), height=4,
                                   yscrollcommand=sb.set, bg="white",
                                   selectbackground="#bbdefb", relief="solid", bd=1)
        self.listbox.pack(fill="x", expand=True)
        sb.config(command=self.listbox.yview)

        file_btns = tk.Frame(list_frame, bg=BG)
        file_btns.pack(anchor="w", pady=(2, 0))
        tk.Button(file_btns, text="Remove Selected", command=self._remove,
                  relief="flat", bg="#e0e0e0", padx=8, pady=3).pack(side="left")
        tk.Button(file_btns, text="Clear All", command=self._clear,
                  relief="flat", bg="#e0e0e0", padx=8, pady=3).pack(side="left", padx=6)

        # Preset
        self.pre_lf = tk.LabelFrame(self, text=" Preset ", bg=BG,
                                     font=("Segoe UI", 9), fg="#555")
        self.pre_lf.pack(fill="x", padx=12, pady=(4, 2))
        self.preset = tk.StringVar(value="medium")
        pre_row = tk.Frame(self.pre_lf, bg=BG)
        pre_row.pack(anchor="w", padx=8, pady=4)
        for label, val in [("Low", "low"), ("Medium", "medium"),
                            ("High", "high"), ("Custom", "custom")]:
            tk.Radiobutton(pre_row, text=label, variable=self.preset, value=val,
                           bg=BG, font=("Segoe UI", 9),
                           command=lambda v=val: self._apply_preset(v)
                           ).pack(side="left", padx=(0, 14))

        # Image + PDF options side by side — only shown when Custom is selected
        self.options_frame = tk.Frame(self, bg=BG)

        img_lf = tk.LabelFrame(self.options_frame, text=" Image ", bg=BG,
                                font=("Segoe UI", 9), fg="#555")
        img_lf.pack(side="left", fill="both", expand=True, padx=(0, 4))

        q_row = tk.Frame(img_lf, bg=BG)
        q_row.pack(fill="x", padx=8, pady=(6, 2))
        tk.Label(q_row, text="JPEG quality:", bg=BG, font=("Segoe UI", 9)).pack(side="left")
        self.img_quality = tk.IntVar(value=65)
        self.quality_lbl = tk.Label(q_row, text="65", width=3, bg=BG, font=("Segoe UI", 9))
        self.quality_lbl.pack(side="right")
        tk.Scale(q_row, from_=10, to=95, orient="horizontal", variable=self.img_quality,
                 bg=BG, highlightthickness=0, showvalue=False,
                 command=self._on_quality_change
                 ).pack(side="left", fill="x", expand=True, padx=6)

        dpi_row = tk.Frame(img_lf, bg=BG)
        dpi_row.pack(fill="x", padx=8, pady=(0, 6))
        self.limit_dpi_var = tk.BooleanVar(value=True)
        tk.Checkbutton(dpi_row, text="Limit resolution:", bg=BG, font=("Segoe UI", 9),
                       variable=self.limit_dpi_var,
                       command=self._on_custom_change).pack(side="left")
        self.max_dpi_var = tk.IntVar(value=150)
        tk.Spinbox(dpi_row, from_=72, to=600, increment=50, textvariable=self.max_dpi_var,
                   font=("Segoe UI", 9), width=5,
                   command=self._on_custom_change).pack(side="left", padx=4)
        tk.Label(dpi_row, text="DPI", bg=BG, font=("Segoe UI", 9)).pack(side="left")

        pdf_lf = tk.LabelFrame(self.options_frame, text=" PDF ", bg=BG,
                                font=("Segoe UI", 9), fg="#555")
        pdf_lf.pack(side="left", fill="both", expand=True)
        pdf_row = tk.Frame(pdf_lf, bg=BG)
        pdf_row.pack(anchor="w", padx=8, pady=(4, 6))
        self.remove_meta      = tk.BooleanVar(value=True)
        self.compress_streams = tk.BooleanVar(value=True)
        self.remove_images    = tk.BooleanVar(value=False)
        for text, var in [("Remove metadata",     self.remove_meta),
                           ("Re-compress streams", self.compress_streams),
                           ("Remove thumbnails",   self.remove_images)]:
            tk.Checkbutton(pdf_row, text=text, variable=var, bg=BG, font=("Segoe UI", 9),
                           command=self._on_custom_change).pack(anchor="w", pady=1)

        # Output
        out_lf = tk.LabelFrame(self, text=" Output ", bg=BG,
                                font=("Segoe UI", 9), fg="#555")
        out_lf.pack(fill="x", padx=12, pady=(2, 4))
        out_row = tk.Frame(out_lf, bg=BG)
        out_row.pack(fill="x", padx=8, pady=(6, 6))
        tk.Label(out_row, text="Save to:", bg=BG, font=("Segoe UI", 9)).pack(side="left")
        self.save_mode = tk.StringVar(value="same")
        tk.Radiobutton(out_row, text="Same folder  (_compressed suffix)",
                       variable=self.save_mode, value="same",
                       bg=BG, font=("Segoe UI", 9)).pack(side="left", padx=6)
        tk.Radiobutton(out_row, text="Choose folder…",
                       variable=self.save_mode, value="choose",
                       bg=BG, font=("Segoe UI", 9)).pack(side="left")

        # Compress button
        btn_row = tk.Frame(self, bg=BG)
        btn_row.pack(fill="x", padx=12, pady=(0, 4))
        self.btn = tk.Button(btn_row, text="Compress", command=self._start,
                              relief="flat", bg="#e65100", fg="white",
                              font=("Segoe UI", 9, "bold"), padx=14, pady=3, cursor="hand2")
        self.btn.pack(side="right")

        self.log = LogPanel(self, height=5, bg=BG)
        self.log.pack(fill="both", expand=True, padx=12, pady=(0, 12))

    # ── preset ───────────────────────────────────────────────────────

    def _apply_preset(self, name: str):
        if name == "custom":
            self.options_frame.pack(fill="x", padx=12, pady=2, after=self.pre_lf)
            return
        self.options_frame.pack_forget()
        p = _PRESETS[name]
        self.img_quality.set(p["quality"])
        self.quality_lbl.configure(text=str(p["quality"]))
        self.limit_dpi_var.set(True)
        self.max_dpi_var.set(p["dpi"])
        self.remove_meta.set(p["meta"])
        self.compress_streams.set(p["streams"])
        self.remove_images.set(p["thumbs"])

    def _on_quality_change(self, val: str):
        self.quality_lbl.configure(text=str(int(float(val))))
        self._on_custom_change()

    def _on_custom_change(self, *_):
        self.preset.set("custom")
        self.options_frame.pack(fill="x", padx=12, pady=2, after=self.pre_lf)

    # ── file management ──────────────────────────────────────────────

    def _browse(self):
        paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        self._add_files(list(paths))

    def _add_files(self, paths: list[str]):
        added = 0
        for p in paths:
            if p.lower().endswith(".pdf") and p not in self.files:
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

    # ── compression ──────────────────────────────────────────────────

    def _start(self):
        if not self.files:
            self.log.write("No files queued.", "err")
            return
        if self.save_mode.get() == "choose":
            output_dir = filedialog.askdirectory(title="Select output folder")
            if not output_dir:
                return
        else:
            output_dir = None
        self.btn.configure(state="disabled", text="Compressing…")
        max_dpi = self.max_dpi_var.get() if self.limit_dpi_var.get() else None
        opts = {
            "preset":           self.preset.get(),
            "img_quality":      self.img_quality.get(),
            "max_dpi":          max_dpi,
            "remove_meta":      self.remove_meta.get(),
            "compress_streams": self.compress_streams.get(),
            "remove_images":    self.remove_images.get(),
        }
        threading.Thread(
            target=self._run, args=(list(self.files), output_dir, opts), daemon=True
        ).start()

    def _run(self, files: list[str], output_dir: str | None, opts: dict):
        for i, path in enumerate(files, 1):
            self.after(0, lambda p=path, n=i, t=len(files):
                       self.log.write(f"\n[{n}/{t}] {os.path.basename(p)}", "info"))
            self._compress_one(path, output_dir, opts)
        self.after(0, lambda: self.log.write("\nDone.", "ok"))
        self.after(0, lambda: self.btn.configure(state="normal", text="Compress"))

    def _compress_one(self, path: str, output_dir: str | None, opts: dict):
        try:
            stem     = os.path.splitext(os.path.basename(path))[0]
            out_dir  = output_dir or os.path.dirname(path)
            out_path = os.path.join(out_dir, f"{stem}_compressed.pdf")

            before, after = compress_pdf(
                path, out_path, opts,
                log=lambda m: self.after(0, lambda m=m: self.log.write(m, "info")))
            saved = before - after
            pct   = (saved / before * 100) if before else 0

            if saved > 0:
                self.after(0, lambda a=after, b=before, p=pct, o=out_path:
                           self.log.write_link(
                               f"  ✔ {_human_size(b)} → {_human_size(a)}"
                               f"  (−{p:.1f}%)  →  ",
                               o, "ok", text=os.path.basename(o)))
            else:
                self.after(0, lambda o=out_path:
                           self.log.write_link(
                               "  ✔ Saved (no size reduction)  →  ",
                               o, "ok", text=os.path.basename(o)))

        except Exception as e:
            self.after(0, lambda e=e: self.log.write(f"  ✘ Error: {e}", "err"))
