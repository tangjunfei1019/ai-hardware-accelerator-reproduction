# Code sources and reproduction notes: PyPIM: Integrating Digital Processing-in-Memory from Microarchitectural Design to Python Tensors

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B** (the full simulation backend needs CUDA 12.0 and a GPU with at least 8 GB of VRAM).

## Upstream repository (verified to exist)

- Link: https://github.com/oleitersdorf/PyPIM
- Verified HEAD (2026-11-16): 43affb2
- Repository contents: GPU-accelerated simulator (`csrc`), microarchitectural driver, Python development library (`pypim`), test scripts / benchmarks (`tests`), raw results (`results`), example script `main.py`
- Hardware / software requirements: CUDA 12.0 with a GPU of at least 8 GB DRAM, Python 3.10, a C++17 (or higher) compiler. The Python library itself installs with `pip install -e .`, but the simulation backend cannot run without the GPU.
- License: no LICENSE file was found in the repository root — licence unverified; read the repository's own files before use.

## Reproduction steps

1) git clone https://github.com/oleitersdorf/PyPIM
2) Install the development library from the project directory: `pip install -e .`
3) Verify the install: `python main.py` — expected result `32.0`
4) Run the benchmark test scripts in `tests/` against the GPU-accelerated simulator backend
Expected check: `main.py` should print `32.0`; the tensor operations in the README example (e.g. `x[::2].sum()` returning `4.75`) should match. Full benchmark results are simulator estimates, not silicon measurements.

## What cannot be reproduced from the paper alone

- Simulator estimates must not be equated directly with real memristive PIM chip measurements; the simulated microarchitecture, partitions, and array-direction operations are a model of the hardware, not the hardware.
- On a CPU-only machine the full simulation backend cannot run; only the Python library install and its host-side checks are reachable here.
- The skeleton in this directory does not run the CUDA simulator and does not reproduce the paper's benchmark numbers.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
