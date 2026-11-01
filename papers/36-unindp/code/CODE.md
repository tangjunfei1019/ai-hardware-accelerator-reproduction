# Code notes: UniNDP: A Unified Compilation and Simulation Tool for Near DRAM Processing Architectures

- **Upstream repository:** https://github.com/UniNDP-hpca25-ae/UniNDP
- **Licence:** MIT
- **Hardware/software requirements:** Standard Linux CPU + Python; no UPMEM, GPU, or FPGA hardware needed

## Completeness checklist

- Completeness: MIT licence; `compile.py`, `compile_detail.py`, `compile_predictor.py`, `frontend/`, `midend/`, `backend/`, `sim/`, `tools/`, `script/`; `workload/` CSVs; `config/` for upmem, hbm-pim, gddr6-aim, dimmining; tests `testsim.py`, `sim_verify.py`.
- Upstream HEAD verified via `git ls-remote` as c8b21684, also mirrored at godfather991/UniNDP.
- What this local reproduction does not cover: the paper's full per-architecture, per-workload tables, which need the original paper and the upstream workload scripts; toy-scale output is not a paper number.

## Minimal reproduction commands

See the "Reproduction points" section of this paper's README; commands and expected checks follow the upstream README.

## Skeleton note

- `reproduce.py` is an original skeleton using only the Python standard library, not upstream code; it demonstrates the core idea and does not reproduce the original paper's performance numbers.
- Reproducing the original numbers needs the upstream code, the corresponding hardware/toolchain, and the original data/configuration; the skeleton can only verify correctness and relative trends at the algorithm and dataflow level.

