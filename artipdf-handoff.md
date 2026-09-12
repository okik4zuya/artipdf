# ARTi Framework — context handoff for `artipdf`

This project is **Phase 3a of the ARTi Framework** (`~/.arti`, the researcher's ARTi research-workflow
package). Paste this file into `artipdf`'s own `CLAUDE.md` (or read it once at project start) so its
Claude session understands where this tool sits in the larger framework.

## What ARTi is

ARTi is a cross-project research workflow package: skills (`ARTi-idea`, `ARTi-writing`, `ARTi-setup`,
`ARTi-figure`) plus standalone tools, living at `~/.arti` and junction-linked into `~/.claude/skills/`.
Its operating loop is three steps — **Amati → Replikasi → Tambah inovasi** ("observe → replicate →
add innovation") — feeding a publication loop back into the next idea. The ARTi logo (a single
ascending step-path capped by a dot) visualizes exactly that loop.

## What this project is

`artipdf` is the **rebrand of the researcher's existing `uglypdf` tool** into "ARTi PDF" — the
literature-PDF toolkit for the framework. It is tracked as ARTi's own Phase 3a
(`~/.arti/memory/todo-list.md`, "Phase 3 — ARTi PDF + one-page checklist").

**Do not confuse this with `~/.arti/tools/arti-pdf/`** — that is a small, already-finished,
one-direction Markdown→A4-PDF converter (zero-install, stdlib Python + headless Edge/Chrome print)
used internally by ARTi-idea/ARTi-writing to render frozen reference docs like the Research Design or
Completion Plan. It stays as-is; it is not this project and does not need to be merged into it.

### Original scope (from the ARTi backlog, not yet built beyond planning)
- Bulk **PDF → Markdown**, with two features called out explicitly as the trust-making bar:
  - **table fidelity**
  - **equation fidelity** (LaTeX/MathML output)
  - batch/bulk handling for a stack of downloaded papers (this is a literature-review tool, not a
    single-file converter)
- Bulk **Markdown → PDF** (journal-formatted manuscript export)
- **Merge** (manuscript + supplementary + response-to-reviewers → one submission package)
- **Split** (pull one figure-heavy section out of a large PDF)
- A lightweight **editor** (page order, redaction, annotation)
- Every feature should be validated against a **real literature-review workload**, not synthetic
  test PDFs.

### Open decision — not yet made
Implementation approach (native app / CLI / web tool) has **not been decided**. If this comes up,
flag it back rather than assuming — the ARTi backlog explicitly lists it as an open decision, with
"rebrand `uglypdf` → ARTi PDF, add a file-explorer feature" noted as one candidate approach to weigh
against building fresh.

## Branding — already locked, reuse it

The ARTi PDF sub-icon is already designed and exported — don't redesign it:
- Source: `~/.arti/logo/logo-arti-pdf-icon.svg` (exact copy of the locked ARTi mark, unchanged, plus
  a small blue "PDF" badge bottom-right).
- Full PNG/ICO export set at `~/.arti/logo/export/pdf-icon/` (16 through 1024px, favicon.ico,
  apple-touch-icon, android-chrome sizes, and a Windows `arti-pdf.ico`).
- Palette: slate `#475569` (step-path), blue `#2563eb` (dot / badge), off-white `#f7f8fa` background.
- Known limitation: the "PDF" badge reads clearly from 48px up; below that it blurs into a plain blue
  blob and only the base ARTi mark remains recognizable — expected at favicon scale, not a defect.

## Where the source of truth lives

This handoff is a snapshot — for anything current, read these directly in `~/.arti`:
- `memory/todo-list.md` — Phase 3a checklist (authoritative, checkboxes only)
- `memory/status.md` — narrative of what's been decided/built and why
- `memory/memories/branding-logo.md` — full logo/icon design history
- `memory/MEMORY.md` — index into everything else

If `artipdf` reaches a milestone (scope decided, first feature built, etc.), that should be reported
back so `~/.arti/memory/todo-list.md`/`status.md` can be updated — they are the authoritative tracker
for the whole ARTi package, not just this sub-tool.
