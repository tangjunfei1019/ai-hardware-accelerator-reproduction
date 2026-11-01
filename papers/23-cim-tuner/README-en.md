# CIM-Tuner: Balancing the Compute and Storage Capacity of SRAM-CIM Accelerator via Hardware-mapping Co-exploration

## Original paper information

- Original title: CIM-Tuner: Balancing the Compute and Storage Capacity of SRAM-CIM Accelerator via Hardware-mapping Co-exploration
- Authors: Jinwu Chen, Yuhui Shi, He Wang, Zhe Jiang, Jun Yang, Xin Si, Zhenhua Zhu
- Year and venue: arXiv 2026
- arXiv / DOI: arXiv:2601.18070

## Core method

- Uses a matrix abstraction to unify multiple CIM macros, and a general accelerator template for hardware-mapping co-exploration: under an area constraint, hardware configuration and mapping strategy are searched together to balance compute capacity and storage capacity, rather than fixing hardware first and then fitting a mapping to it.

## Core results

- As reported in the paper (see the original): expanding the strategy space gives about 1.58x energy-efficiency and about 2.11x throughput improvement over existing CIM mappings; comparable improvements over existing CIM accelerators under the same area budget; the paper states its simulation accuracy was silicon-validated — see the original for details.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
