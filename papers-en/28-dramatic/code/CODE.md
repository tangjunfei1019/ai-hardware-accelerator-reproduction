# Code sources and reproduction notes: DRAMatic Speedup: Accelerating HE Operations on a Processing-in-Memory System

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B**.

## Upstream repository (verified to exist)

- Link: https://github.com/UzL-ITS/DRAMatic-Speedup
- Repository contents: C++ UPMEM DPU code, homomorphic-encryption primitives (BGV multiplication, NTT / iNTT, modular addition / multiplication), RNS-optimized implementations
- Hardware / software requirements: full speed reproduction needs UPMEM PIM hardware (DPU DIMMs) and the UPMEM SDK; without hardware, code can only be compiled and read — the paper's hardware speedup cannot be reproduced
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/UzL-ITS/DRAMatic-Speedup
2) Install the UPMEM SDK per the repository instructions and confirm the DPU toolchain works
3) On a machine with UPMEM hardware, compile and run a minimal NTT / modular-multiplication example
4) Then run the BGV multiplication case and compare against the paper's parameters and baselines
Expected check: the minimal example should correctly complete NTT / iNTT round-trips on a DPU; without hardware, record explicitly that the hardware part was not reproduced.

## What cannot be reproduced from the paper alone

- The 334x hardware speedup cannot be reproduced on an ordinary CPU; CPU simulation results must not be treated as DPU measurements; power numbers are only comparable under UPMEM hardware measurement conditions.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
