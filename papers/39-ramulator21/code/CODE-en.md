# Code notes: Ramulator 2.1: A Composable Memory System Simulator for Modern DRAM Systems

- **Upstream repository:** https://github.com/CMU-SAFARI/ramulator2
- **Licence:** MIT
- **Hardware/software requirements:** Standard Linux CPU + C++ toolchain (cmake, GCC) + Python 3.10+; no GPU, FPGA, or DRAM hardware needed

## Completeness checklist

- Completeness: MIT licence; C++ `src/` (DRAM, controller, frontend, memory system, power, translation), `python/` (auto-generated wrappers), `tests/` (unit, controller scheduling, device timings, latency–throughput, power, smoke), `examples/`, visualizer; gem5 integration.
- Upstream HEAD verified via `git ls-remote` as 1bb52cee.
- What this local reproduction does not cover: the full test suite and gem5 integration validation, which need longer runs and a gem5 environment.

## Minimal reproduction commands

See the "Reproduction points" section of this paper's README; commands and expected checks follow the upstream README.

## Skeleton note

- `reproduce.py` is an original skeleton using only the Python standard library, not upstream code; it demonstrates the core idea and does not reproduce the original paper's performance numbers.
- Reproducing the original numbers needs the upstream code, the corresponding hardware/toolchain, and the original data/configuration; the skeleton can only verify correctness and relative trends at the algorithm and dataflow level.

