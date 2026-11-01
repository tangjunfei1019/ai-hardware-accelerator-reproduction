# Code sources and reproduction notes: XBTorch: A Unified Framework for Modeling and Co-Design of Crossbar-Based Deep Learning Accelerators

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/ADAM-Lab-GW/xbtorch
- Repository contents: PyTorch-native crossbar modeling library, device models (FeFET / ReRAM / PCM / MTJ), hardware-aware training and inference examples, documentation
- Hardware / software requirements: a standard CPU can run small examples; large models are best run on a GPU. Python 3.10+ and PyTorch, see the upstream README
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/ADAM-Lab-GW/xbtorch
2) pip install torch (matching the upstream requirements / documentation versions)
3) Follow the upstream documentation for a minimal example: define a device model, map a linear layer to a crossbar, and run one noisy inference
4) Then run a hardware-aware training example and compare against the no-noise baseline
Expected check: without noise, results should be close to ideal accuracy; after injecting device noise, accuracy should drop, and hardware-aware training should partially recover it.

## What cannot be reproduced from the paper alone

- FeFET measured device parameters cannot be reproduced with this directory's Python standard-library skeleton; simulation accuracy must not be equated directly with chip-measured accuracy; device parameters follow the paper and upstream examples.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
