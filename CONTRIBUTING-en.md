# Contributing

Chinese version: [CONTRIBUTING.md](CONTRIBUTING.md). This guide codifies rules already applied in this repository. New contributions should follow the same rules, not invent a new layout.

## One paper = one folder

- Folder name: `papers/NN-YYYYMM-slug/`, e.g. `papers/01-201712-sze-survey/`. `NN` is the sequential number; the next one is 40.
- `YYYYMM` is the month of the paper's first publication, conference, journal issue, or open-source release, and must be verified. If only the year can be verified, use the placeholder `202600` and say so in the paper README. Do not invent a month, and do not present an arXiv month as a journal month (the one existing exception, paper 26 using an arXiv month as a fallback, was explicitly flagged when it was approved).
- Inside each paper folder:
  - Analysis, bilingual side by side: `README.md` (Chinese) + `README-en.md` (English), with the same core method, numbers, links, and code provenance in both versions.
  - Code and reproduction, English only: `code/CODE.md` + `code/reproduce.py`. Do not recreate `CODE-en.md` / `reproduce-en.py`; those duplicates were deleted on 2026-11-02.

## Label code provenance honestly

- `code/CODE.md` must state clearly whether the code is: official / third-party / simulation tool / skeleton only / not found, with verified links.
- `code/reproduce.py` is by default an original skeleton using only the Python standard library, for understanding the core idea (tiling, dataflow, sparsity, systolic arrays, compute-in-memory, and so on). It is not the original paper code and not RTL, and it cannot reproduce the original area, power, or clock numbers. Never present a skeleton, a third-party implementation, or a simulation tool as the original code.
- Do not copy upstream code into this repository. Upstream projects are collected as links only in `external/README.md`; to follow their updates, run `bash external/sync-external.sh`, which pulls them into the local, gitignored `external-checkouts/` directory and does not commit them.
- Before copying or redistributing any upstream code, check its licence. Projects marked "not verified" in `external/README.md` must not be redistributed until their licence is verified.

## Rules for numbers

- Peak performance must carry a label: **paper-claimed** / **model estimate** / **not given**. A relative speedup, bandwidth, or energy-efficiency figure is not a peak; do not enter it as one.
- A cell with no number stays "not given". Do not invent one. If a precision bit-width is not stated, say so.
- When adding or changing a paper, update the same row in both [COMPARISON.md](COMPARISON.md) and [COMPARISON-en.md](COMPARISON-en.md), keeping the columns identical: workload, dataflow/architecture, precision, peak (with label), code type, runnable here.

## Real runs need evidence

- A skeleton must run locally before it is submitted. A text-only change must not be described as runnable.
- A real upstream run (such as AIHWKit or ColumnQuant) must be filed as `runs/<name>-YYYYMMDD/` with the command, log, result, and scope, and linked from that paper's `code/CODE.md`. Such evidence proves only that the toolchain or module runs, unless a full training or evaluation flow was completed; it does not by itself reproduce a paper's accuracy table.
- The unified comparable path lives in `unified/` (SCALE-Sim v3): a new comparable run must use the same workload, state the array, dataflow, and bandwidth mode, and be labelled a framework estimate, not a paper number and not silicon measurement. Runs with different workloads or bandwidth modes must not share one comparison table.

## Three good first contributions

1. Fill one "not given" cell in the comparison matrix, citing a source inside the paper folder, without importing an unsourced number.
2. Add a new paper following this template (bilingual analysis + English skeleton + one comparison-matrix row), with the skeleton run first.
3. File a `runs/` evidence folder for an upstream run that already works locally, and link it from the corresponding `CODE.md`.

## Pre-submission checklist

- [ ] Folder name matches `NN-YYYYMM-slug`; the month has a source, or `202600` is used and explained.
- [ ] Chinese and English analysis agree; code files are English-only with no leftover Chinese.
- [ ] Code provenance is labelled correctly; no skeleton is presented as original code or RTL.
- [ ] Peak numbers carry labels; "not given" cells contain no invented numbers.
- [ ] Both comparison-matrix versions are updated in sync; any real run has a `runs/` evidence folder and a link.
- [ ] The skeleton runs; no upstream code was copied in, and `external-checkouts/` was not committed.
