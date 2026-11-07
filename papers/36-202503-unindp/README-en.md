# UniNDP: A Unified Compilation and Simulation Tool for Near DRAM Processing Architectures

## Original paper information

- **Authors:** Tongxin Xie, Zhenhua Zhu, Bing Li, et al. (Tsinghua University and collaborators)
- **Venue:** HPCA 2025 (Best Paper Honorable Mention)
- **Upstream repository:** https://github.com/UniNDP-hpca25-ae/UniNDP
- **Licence:** MIT
- **Hardware/software requirements:** Standard Linux CPU + Python; no UPMEM, GPU, or FPGA hardware needed

## Core method

- A unified tree-based near-DRAM processing (NDP) hardware abstraction and a unified instruction set, describing different DRAM technologies and processing-unit placements with one model instead of one stack per vendor.
- A cycle-accurate, instruction-driven simulator that tracks memory elements and processing units, giving the compiler a performance predictor.
- A compiler that optimises data partitioning, mapping, and workload scheduling, with hardware-status-guided search-space pruning.
- Architectures covered include UPMEM, Samsung HBM-PIM, SK Hynix GDDR6-AiM, and AxDIMM; example workloads include ResNet-18, VGG-11, LLaMA-2 7B/13B prefill and decode, and plain matrix multiplication.

## Core results

- The paper reports 1.05–3.43x speedup over existing mapping/compilation methods across architectures and ML workloads (source summaries differ slightly: the slide deck gives 1.08–3.37x; the paper is authoritative).
- The more important effect is methodological: the same NDP idea can be compared across architectures instead of being locked to one vendor's simulation/compilation stack.
- This repository does not treat the tool's toy-scale output as a paper number: the 16x16 matmul in the reproduction notes below only proves that the compile-plus-simulate pipeline runs.

## Reproduction points

- Minimal reproduction (actually run here): `git clone https://github.com/UniNDP-hpca25-ae/UniNDP.git`, `pip install -r requirements.txt` (numpy, PyYAML, tqdm, xlrd, xlsxwriter), `python compile.py -h` prints the full compiler options, and `python compile.py -A upmem -W mm -S 16 16 16 1 -O testout` writes CSV and log under `test/testout/`.
- Observed result: the tiny UPMEM 16x16x16 matmul wrote `test/testout/csv/_gemm.csv`, with `best_result: 98` and `speedup: 1.0` in the log. For a 16x16 toy problem, 1.0x over its own baseline is unsurprising; the point is that the compile-plus-simulate pipeline runs end to end.
- Honest note: the tool exits non-zero at the very end in this environment, after the CSV is written, so treat the CSV/log as the check, not the exit code. Full workloads (ResNet/LLaMA CSVs) were not run; those are the longer, paper-scale runs.

## Code sources

- Upstream code is at the repository link above; `code/CODE.md` in this folder gives the completeness checklist and minimal reproduction commands.
- **`code/reproduce.py` in this folder is an original reproduction skeleton using only the Python standard library, for understanding the core idea. It is not upstream code, and it is not the original hardware/simulator, and it cannot directly reproduce the original paper's numbers.**

