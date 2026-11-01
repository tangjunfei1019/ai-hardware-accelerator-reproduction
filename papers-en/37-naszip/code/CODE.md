# Code notes: NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing

- **Upstream repository:** https://github.com/Intelligent-Computing-Research-Group/NasZip
- **Licence:** MuLan PSL 2.0 (badge in README; check the repo's licence file before redistribution)
- **Hardware/software requirements:** Pre-built-index route: x86 server with 16+ CPU cores and 256+ GB DRAM; build-from-scratch route needs a large-VRAM GPU and much more time

## Completeness checklist

- Completeness: MuLan PSL 2.0 badge in README; `simulate/` (cache, detail, FEE, overall, prefetch simulators), `sim_tools/`, `idx_tools/`, `preprocess_idx/`, plotting scripts in `Plot/`, `result/` with pre-filled baseline data; per-figure bash scripts with stated runtimes; the paper's artifact appendix cites a Zenodo archive, DOI 10.5281/zenodo.19453078.
- Upstream HEAD verified via `git ls-remote` as a1e96eae.
- What cannot be reproduced on this machine: the full paper-scale simulations and the Fig. 8/15/16/19 pipelines, which need a qualifying server and large data downloads.

## Minimal reproduction commands

See the "Reproduction points" section of this paper's README; commands and expected checks follow the upstream README.

## Skeleton note

- `reproduce.py` is an original skeleton using only the Python standard library, not upstream code; it demonstrates the core idea and does not reproduce the original paper's performance numbers.
- Reproducing the original numbers needs the upstream code, the corresponding hardware/toolchain, and the original data/configuration; the skeleton can only verify correctness and relative trends at the algorithm and dataflow level.

