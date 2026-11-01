## Code sources

- Status: **Simulation tool, no official chip code for this paper**. This paper is a survey and does not come with chip RTL.
- Closest modeling routes (verified to exist):
  - Timeloop / Accelergy infrastructure: https://github.com/Accelergy-Project/accelergy-timeloop-infrastructure
  - Timeloop / Accelergy exercises: https://github.com/Accelergy-Project/timeloop-accelergy-exercises
- Nature: third-party academic tools (modeling frameworks from MIT and other institutions), not chip code released by the authors of the Sze survey; read each repository's own license before use.
- How to run: first use this directory's `reproduce.py` to understand data-movement accounting, then use Timeloop to define an architecture and mapping and compare memory accesses and energy under different dataflows.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, using only the Python standard library, demonstrating memory-access accounting under three dataflows. It is not the original paper code.
