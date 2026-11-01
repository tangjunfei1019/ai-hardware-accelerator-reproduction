# Ramulator 2.1: A Composable Memory System Simulator for Modern DRAM Systems

## Original paper

- **Authors:** Haocong Luo, F. Nisa Bostancı, Ataberk Olgun, et al. (SAFARI Research Group, ETH Zürich and collaborators)
- **Venue:** 2026 (Tutorial on Ramulator and DRAM Bender, colocated with ICS); arXiv:2606.13844
- **Upstream repository:** https://github.com/CMU-SAFARI/ramulator2
- **Licence:** MIT
- **Hardware/software requirements:** Standard Linux CPU + C++ toolchain (cmake, GCC) + Python 3.10+; no GPU, FPGA, or DRAM hardware needed

## Core method

- **Scope note: this is not a CIM accelerator paper. It is the DRAM/memory-system simulator** that CIM and near-data-processing research depends on to evaluate anything that touches DRAM, which is why it earns a place in this set; it must not be presented as a CIM architecture.
- A clean, modular C++ codebase with automatically generated Python wrappers: users write high-level DRAM specifications in Python and the framework generates the Python proxies, hiding low-level C++ boilerplate.
- Cycle-level DRAM device and memory-controller models, usable standalone on memory traces or as a library inside other simulators (gem5 wrappers provided, SE and FS modes).
- Validation at two levels: fine-grained timing-constraint/scheduling checks and system-level latency–throughput curves; plus a trace visualizer for DRAM command traces.
- Modern standards covered include DDR3/4/5, GDDR6/7, LPDDR5/6, HBM1–4, and DDR4_PUM (processing-using-DRAM), which is key for CIM research.

## Core effect

- Its value is measured by coverage, usability, and validation, not by TOPS/W: this is a simulator, not an accelerator, so no speedup is quoted here.
- The SAFARI group's Ramulator line is the standard DRAM simulator in the memory-systems literature; the 2026 overhaul adding HBM4, LPDDR6, GDDR7, and DDR4_PUM support is evaluation infrastructure that later CIM work will build on.
- Validation results in the paper/tutorial are authoritative in the original; the statistics run here are the example trace's own numbers, not a paper result.

## Reproduction points

- Minimal reproduction (actually run here): `git clone https://github.com/CMU-SAFARI/ramulator2.git`, `bash build.sh` (cmake configure + build; configure took about 44 s here, full build several minutes), `PYTHONPATH=$PWD/python python3 examples/example_config.py`.
- Observed result: configure completed (cmake, GCC 13.3, Python 3.12.3, 14 DRAM standards generated, 52 Python component wrappers generated), the build completed, and the example ran: Controller cycles 81302, avg read latency 45.2 cycles, read requests 6, write requests 0, row hits 3, row misses 3, row conflicts 0.
- Honest note: these are the example trace's own statistics, not a paper result; the full test suite (`tests/`) was not run — that is the longer validation route.

## Code source

- Upstream code is at the repository link above; `code/CODE.md` in this folder gives the completeness checklist and minimal reproduction commands.
- **`code/reproduce.py` in this folder is an original reproduction skeleton using only the Python standard library, for understanding the core idea. It is not upstream code, and it is not the original hardware/simulator, and it cannot directly reproduce the original paper's numbers.**

