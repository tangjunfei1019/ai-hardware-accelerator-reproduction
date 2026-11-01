# Code sources and reproduction notes: Characterizing Digital DRAM PIM through Modeling and Benchmarking (PIMeval-PIMbench extension, TACO 2026)

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/UVA-LavaLab/PIMeval-PIMbench
- Repository contents: C++ PIMeval simulator, PIMbench benchmark suite, three digital PIM models (subarray-level bit-serial / bit-parallel and bank-level bit-parallel), roofline analysis tools
- Hardware / software requirements: standard Linux machine, C++ toolchain; no UPMEM hardware is needed to run the simulator and benchmarks (real-hardware comparisons need separate explanation)
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/UVA-LavaLab/PIMeval-PIMbench
2) Build the simulator and benchmarks per the repository wiki / README
3) First run a minimal benchmark to confirm the three PIM models can be switched
4) Then run the roofline analysis and compare against the paper's method
Expected check: minimal benchmarks should output latency and energy estimates; the roofline should show PIM vs CPU / GPU crossover trends as arithmetic intensity changes.

## What cannot be reproduced from the paper alone

- Simulator estimates must not be equated directly with real DRAM PIM chip measurements; DRAM technology parameters (DDR / HBM, GDL width) affect conclusions and must not be ignored.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
