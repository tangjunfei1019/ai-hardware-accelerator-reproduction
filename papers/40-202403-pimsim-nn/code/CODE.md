# Code sources and reproduction notes: PIMSIM-NN: An ISA-based Simulation Framework for Processing-in-Memory Accelerators

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B** (C++/SystemC build; new instructions need the pimcomp-nn compiler).

## Upstream repository (verified to exist)

- Link: https://github.com/wangxy-2000/pimsim-nn
- Verified HEAD (2026-11-16): 3e3442b
- Repository contents: C++/SystemC cycle-accurate simulator (executable `ChipTest`), built-in ResNet-18 example (configuration and instruction files), architecture and NoC configuration files
- Hardware / software requirements: cmake >= 3.6, gcc >= 4.8.5; SystemC-based build. New instructions must be generated from an ONNX model by the companion compiler https://github.com/sunxt99/PIMCOMP-NN
- License: no LICENSE file was found in the repository root — licence unverified; read the repository's own files before use.

## Reproduction steps

1) git clone https://github.com/wangxy-2000/pimsim-nn
2) Build with cmake: `mkdir build && cd build && cmake .. && make` (executable `ChipTest`)
3) Run the built-in ResNet-18 example: `./ChipTest ../example/resnet18.gz ../example/config/latency_config.json`
4) To simulate a new network, generate its instruction sequence with pimcomp-nn from an ONNX file using the same architecture configuration
Expected check: the simulator should print a simulation report with core count, throughput (the README example reports 40 samples/s on 64 cores) and average latency (25 ms in the example); these are simulator estimates, not silicon measurements.

## What cannot be reproduced from the paper alone

- Simulator estimates must not be equated directly with real RRAM PIM chip measurements; architecture and NoC configuration parameters (latency and power of each component) drive the results and must not be ignored.
- The skeleton in this directory does not run the SystemC simulator and does not reproduce the paper's latency or power numbers.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
