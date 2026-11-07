# OpenACM: An Open-Source SRAM-Based Approximate CiM Compiler

## Original paper information

- Original title: OpenACM: An Open-Source SRAM-Based Approximate CiM Compiler
- Authors: Yiqi Zhou, JunHao Ma, Xingyang Li, Yule Sheng, Yue Yuan, Yikai Wang, Bochang Wang, Yiheng Wu, Shan Shen, Wei Xing, Daying Sun, Li Li, Zhiqiang Xiao
- Year and venue: DATE 2026
- arXiv / DOI: arXiv:2601.11292

## Core method

- Systematically brings approximate computing into an SRAM digital CIM compiler: provides exact, tunable-approximate, and logarithmic multiplier libraries, trading accuracy against energy within an application's fault tolerance; the compiler automatically generates DCIM architectures, and connects transistor-level customizable SRAM macros and variation-aware characterization into a complete physical flow based on OpenROAD and FreePDK45.

## Core results

- As reported in the paper (see the original): up to about 64% energy saving on representative CNNs, with negligible application accuracy loss; specific models and approximate configurations follow the original.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Run evidence

- The minimal front-end generators were actually run (2026-11-05): the 8-bit multiplier step generated three RTL files, `Exact_8bit.v`, `Appro4_2_8bit.v` and `Log_our_8bit.v`; the 8-bit / 16-deep SRAM step exited 0 but changed nothing, because the shipped `sram.v` already is the 16x8 module. Evidence: [runs/openacm-20261105/](../../runs/openacm-20261105/). This proves only that the current v2 front end can generate 8-bit multiplier RTL, not any DATE 2026 paper numbers, and it is not a silicon measurement; the PE and backend flow were not attempted.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
