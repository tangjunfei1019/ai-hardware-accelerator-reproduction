# Code sources and reproduction notes: A gem5-based Simulation Framework for Computing-in-DRAM (gem5-CIMD)

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/tud-ccc/gem5-CIMD
- Repository contents: CIMD simulator based on a recent gem5, 16 CIM instructions, a CIM standard library, a custom CIM memory allocator, KNN and other evaluation workloads
- Hardware / software requirements: standard Linux machine, C++ toolchain and gem5 build environment (SCons and others, see upstream documentation); build time is long — this is a simulator, not real DRAM hardware
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/tud-ccc/gem5-CIMD
2) Install gem5 build dependencies per the upstream documentation and build (allow a long build time)
3) First run the repository's built-in minimal CIMD example to confirm the instructions and allocator work
4) Then run the end-to-end KNN case and compare against the paper's method description
Expected check: the minimal example should correctly complete in-subarray bit operations; KNN should output classification results and simulation statistics.

## What cannot be reproduced from the paper alone

- Cycle-accurate gem5 statistics cannot be reproduced with this skeleton; simulator results must not be equated directly with commercial DRAM chip measurements; real DRAM device behavior follows the paper and the MIMDRAM / SIMDRAM literature.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
