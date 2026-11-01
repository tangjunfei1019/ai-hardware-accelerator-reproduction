# DRAMatic Speedup: Accelerating HE Operations on a Processing-in-Memory System

## Original paper information

- Original title: DRAMatic Speedup: Accelerating HE Operations on a Processing-in-Memory System
- Authors: Niklas Klinger, Jonas Sander, Peterson Yuhala, Pascal Felber, Thomas Eisenbarth
- Year and venue: arXiv 2026
- arXiv / DOI: arXiv:2602.12433

## Core method

- Implements homomorphic-encryption primitives on general-purpose UPMEM PIM: uses residue number system (RNS) and number-theoretic transform (NTT) optimizations for polynomial arithmetic, avoiding weak DPU multiplication and expensive inter-core communication, supporting the large parameters needed for secure evaluation; and gives the first power measurements for this workload class on UPMEM.

## Core results

- As reported in the paper (see the original): about 334x speedup over the previous homomorphic-encryption implementation on UPMEM; the gap to Microsoft SEAL is significantly narrowed, but results remain constrained by data-transfer overhead and DPU multiplication performance. See the original for details.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
