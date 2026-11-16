# Code sources and reproduction notes: CiMLoop: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B** (Docker container with Timeloop + Accelergy v4; Timeloop/Accelergy tutorials are a prerequisite).

## Upstream repository (verified to exist)

- Link: https://github.com/mit-emze/cimloop
- Verified HEAD (2026-11-16): 481c044
- Repository contents: tutorials, examples, documentation, and the paper artifact (notebooks reproducing the paper's results); project website https://emze.csail.mit.edu/cimloop
- Hardware / software requirements: Docker (amd64 supported; arm64 is not stable per the repository README). The Timeloop and Accelergy tutorials are a prerequisite.
- License: MIT.
- Maintenance status: the repository homepage states it is **no longer maintained**; the architecture models moved to https://github.com/Accelergy-Project/accelforge (AccelForge) and the component models to https://github.com/Accelergy-Project/hwcomponents (HWComponents). The old repository is kept for archival and reproducibility only — use AccelForge and HWComponents for future work.

## Reproduction steps

1) git clone https://github.com/mit-emze/cimloop
2) cd cimloop && export DOCKER_ARCH=amd64 && docker-compose pull && docker-compose up
3) Inside the container, follow the workspace README; complete the Timeloop/Accelergy tutorials first, then the CiMLoop tutorials in `workspace/tutorials`
4) Reproduce the paper's results with the `models/arch/1_macro/*/_guide.ipynb` notebooks and `tutorials/demo_speed_accuracy.ipynb`
Expected check: the notebooks should reproduce the paper's modelling results; the demo notebook compares the fast statistical model against the accurate model.

## What cannot be reproduced from the paper alone

- Model estimates must not be equated directly with fabricated CiM chip measurements; the energy model depends on operand values, data representations, and circuit parameters, which must not be ignored.
- The unmaintained repository may drift from its successor tools; for new work, the maintained AccelForge / HWComponents repositories are the correct target.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
