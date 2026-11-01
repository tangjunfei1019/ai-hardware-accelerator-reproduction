# Characterizing Digital DRAM PIM through Modeling and Benchmarking (PIMeval-PIMbench extension, TACO 2026)

## Original paper information

- Original title: Characterizing Digital DRAM PIM through Modeling and Benchmarking (PIMeval-PIMbench extension, TACO 2026)
- Authors: Farzana Ahmed Siddique, et al. (follow the paper's author list)
- Year and venue: ACM TACO, 2026
- arXiv / DOI: as in the original

## Core method

- Extends PIMeval / PIMbench: supports a wider range of workloads, PIM architectures, and DRAM technologies, covering three classes of digital PIM — subarray-level bit-serial, subarray-level bit-parallel, and bank-level bit-parallel; adds roofline analysis and in-kernel execution-phase breakdown to find the crossover points between PIM and CPU / GPU; and analyzes the effects of DRAM variants such as DDR / HBM and GDL width.

## Core results

- As reported in the paper (see the original): a systematic method giving the applicable ranges and crossover points of the three digital PIM classes, rather than a single speedup number; specific model and benchmark numbers follow the paper's tables, and this directory does not treat skeleton roofline slopes as paper results.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
