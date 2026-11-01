## Code sources

- Status: **Simulation tools, no official ISAAC code**. No confirmed public repository for the original ISAAC implementation was found in this check.
- Verified modeling tools:
  - DNN NeuroSim V1.4 (inference side): https://github.com/neurosim/DNN_NeuroSim_V1.4
  - DNN NeuroSim V2.1 (on-chip training side): https://github.com/neurosim/DNN_NeuroSim_V2.1
- Nature: a widely used academic compute-in-memory benchmark framework, not original code released by the ISAAC authors; read each repository's own license before use, and note the version differences (V1.x and V2.x have different focuses).
- This directory contains only an original reproduction skeleton, and no copy of any upstream code.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, using only the Python standard library, demonstrating crossbar MVM and bit-slicing. It is not the original paper code.
