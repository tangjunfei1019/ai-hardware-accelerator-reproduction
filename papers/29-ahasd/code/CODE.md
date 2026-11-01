# Code sources and reproduction notes: AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/MAdrid1011/AHASD
- Repository contents: C++ simulator, adaptive drafting speculative decoding algorithm, NPU-PIM asynchronous scheduling implementation
- Hardware / software requirements: standard machine + simulator toolchain (ONNXim and SAIT PIM simulator, see the paper and upstream documentation); no real mobile PIM chip is needed to run the simulation, but simulation must not be equated with mobile measurements
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/MAdrid1011/AHASD
2) Install simulator dependencies per the upstream documentation (ONNXim / SAIT PIM simulator configuration)
3) First run the repository's built-in small example to confirm the draft-verify asynchronous pipeline
4) Then run the paper's LLM and adaptive drafting algorithm configurations and compare against the paper's baselines
Expected check: small examples should output acceptance rates and throughput trends; the asynchronous mode should reduce idle time versus the synchronous mode.

## What cannot be reproduced from the paper alone

- Simulator throughput must not be treated as mobile measured throughput; baseline GPU models and simulator configuration differences must not be ignored; real LPDDR5-PIM hardware results follow the original.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
