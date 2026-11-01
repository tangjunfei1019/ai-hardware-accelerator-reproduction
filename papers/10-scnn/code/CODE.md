## Code sources

- Status: **Simulation tool; the paper's cycle-level simulator was not released**. Do not label any third-party SCNN replica as the original authors' official code.
- Verified modeling tool:
  - Sparseloop MICRO22 artifact: https://github.com/Accelergy-Project/micro22-sparseloop-artifact (Sparseloop can model sparse tensor accelerators including SCNN)
- Before use, read that repository's own license and README; Sparseloop is an analytical modeling tool, not SCNN's original cycle-level simulator, and its result basis is different.
- This directory contains only an original reproduction skeleton, and no copy of any upstream code.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, using only the Python standard library, demonstrating compressed sparse convolution and scatter accumulation. It is not the original paper code.
