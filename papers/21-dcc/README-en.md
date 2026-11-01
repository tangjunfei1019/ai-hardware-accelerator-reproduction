# DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures

## Original paper information

- Original title: DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures
- Authors: Peiming Yang, Sankeerth Durvasula, Ivan Fernandez, Mohammad Sadrosadati, Onur Mutlu, Gennady Pekhimenko, Christina Giannoula
- Year and venue: ISCA 2026
- arXiv / DOI: arXiv:2511.15503, 10.1109/ISCA66397.2026.00180

## Core method

- Proposes a multi-level PIM abstraction that abstracts the PIM memory hierarchy as PIM groups, decoupling the compiler from backend semantics; a data-centric scheduling generator maps data tiling strategies to compute loop tiling, jointly optimizing data rearrangement and compute code, and a fast performance prediction model selects the best configuration.

## Core results

- As reported in the paper (see the original): versus GPU execution, up to about 7.68x and on average about 2.7x speedup on HBM-PIM, and up to about 13.17x and on average about 5.75x on AttAcc; end-to-end LLM inference on AttAcc reaches up to about 7.71x and on average about 4.88x speedup. Presentation slides separately give about 1.7x on HBM-PIM and about 1.3x on AttAcc for a single ML kernel versus a default implementation. Do not mix baselines.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
