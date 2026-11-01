## Code sources

- Status: **Simulation tools; Google TPU hardware itself is not open source**. Do not label any third-party TPU replica as Google official code.
- Verified modeling tools:
  - SCALE-Sim: https://github.com/scalesim-project/SCALE-Sim (systolic-array accelerator simulator, Python)
  - Timeloop/Accelergy: https://github.com/Accelergy-Project/accelergy-timeloop-infrastructure
- Before use, read each repository's own license; for SCALE-Sim's old and new versions (the ARM-software version is archived, the scalesim-project version is maintained), follow the repository README.
- This directory contains only an original reproduction skeleton, and no copy of any upstream code.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, using only the Python standard library, demonstrating small systolic-array-style matrix multiplication. It is not the original paper code.
