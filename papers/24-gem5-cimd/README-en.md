# A gem5-based Simulation Framework for Computing-in-DRAM (gem5-CIMD)

## Original paper information

- Original title: A gem5-based Simulation Framework for Computing-in-DRAM
- Authors: Alexander Kusnezoff, João Paulo C. de Lima, Jeronimo Castrillon, Asif Ali Khan
- Year and venue: arXiv 2026
- arXiv / DOI: arXiv:2610.08186

## Core method

- Brings DRAM subarray in-compute (CIMD) into full-application gem5 simulation: extends the instruction set to 16 instructions covering arithmetic, relational, conditional, and utility operations, supporting 4 to 64 bits; multi-level large pages, a CIM-aware allocator, and subarray-aware address mapping ensure operands land in the same subarray.

## Core results

- As reported in the paper (see the original): the framework runs complete applications rather than trace replay only, with end-to-end KNN as the case study; specific speedup and overhead numbers follow the original, and this directory does not treat skeleton bit-operation speed as a gem5 simulation result.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
