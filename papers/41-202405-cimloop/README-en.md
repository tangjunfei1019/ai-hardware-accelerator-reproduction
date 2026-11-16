# CiMLoop: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool

## Original paper information

- Original title: CiMLoop: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool
- Authors: Tanner Andrulis, Joel S. Emer, Vivienne Sze
- Year and venue: ISPASS 2024 (2024-05-05), Best Paper Award
- arXiv / DOI: arXiv:2405.07259; DOI 10.1109/ISPASS61541.2024.00012

## Core method

- A full-stack compute-in-memory (CiM) modeling tool built on Timeloop + Accelergy v4: one flexible specification describes workloads and maps them to circuits and architecture, covering devices, circuits, architecture, workload, and mapping — rather than a single level of the stack or a single design point.
- An accurate energy model that captures the interaction between DNN operand values, hardware data representations, and the analog / digital values propagated by circuits.
- A fast statistical model that explores the design space orders of magnitude more quickly than other high-accuracy models; the repository ships tutorials, examples, and notebooks that reproduce the paper's results (run inside a Docker container).
- Prerequisite: complete the Timeloop and Accelergy tutorials first; the paper's results are reproduced by running the `models/arch/1_macro/*/_guide.ipynb` notebooks and `tutorials/demo_speed_accuracy.ipynb`.

## Core results

- As reported in the paper (see the original): researchers can evaluate design choices at different levels of the CiM stack, co-design across all levels, fairly compare different implementations, and rapidly explore the design space; this directory does not treat skeleton energy estimates as paper results.
- Peak performance: no comparable peak number is given (the statistical model being "orders of magnitude" faster is a relative claim, not a peak).

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers. CiMLoop itself is a modeling tool, and its outputs are model estimates, not silicon measurements; the upstream repository is no longer maintained — its models have moved to AccelForge / HWComponents, and the old repository is kept for archival reproduction only. Use AccelForge and HWComponents for future work.
