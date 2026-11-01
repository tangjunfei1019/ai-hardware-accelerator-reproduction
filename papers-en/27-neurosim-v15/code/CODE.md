# Code sources and reproduction notes: NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/neurosim/NeuroSim
- Repository contents: branches for each version (2D inference / training, 3D inference, MLP inference), TensorRT quantization interface, noise-injection models, device and circuit PPA estimation
- Hardware / software requirements: a standard CPU can run it; a GPU only accelerates simulation and is not required. C++ toolchain; branch selection follows the upstream README; note the non-commercial license (CC BY-NC 4.0)
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/neurosim/NeuroSim
2) Follow the upstream README to select the corresponding version branch and read that branch's user manual
3) First run the branch's built-in small example to confirm the quantization and noise-injection flow
4) Then run ViT / CNN comparison configurations and compare against the paper's method
Expected check: small examples should output accuracy and PPA estimates; with noise off, results should be close to ideal accuracy.

## What cannot be reproduced from the paper alone

- Skeleton noise results must not be treated as NeuroSim simulation results; the framework must not be used commercially (non-commercial license); device parameters follow the paper and branch documentation.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
