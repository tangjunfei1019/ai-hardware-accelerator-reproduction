# TetrisG-SDK: Efficient Convolutional Layer Mapping with Adaptive Windows and Grouped Convolutions for Fast In-Memory Computing

## Original paper information

- Original title: TetrisG-SDK: Efficient Convolutional Layer Mapping with Adaptive Windows and Grouped Convolutions for Fast In-Memory Computing
- Authors: Ke Dong, Kejie Huang, Tao Luo, Bo Wang
- Year and venue: IEEE JETCAS (accepted 2026)
- arXiv / DOI: arXiv:2604.25377

## Core method

- On top of shift-copy kernel (SDK) mapping, introduces adaptive windows: a window can hold more input channels, use marginal space, and adapt to different channel depths; combined with grouped convolutions to reduce compute cycles, and evaluated with a validated CIM hardware simulator giving latency, area, and energy estimates.

## Core results

- As reported in the paper (see the original): versus single-macro VWC-SDK, about 1.2x, 1.3x, and 1.3x speedup on CNN8, GoogLeNet Inception, and DenseNet40 respectively; system-level latency and energy fall about 2.4x and 1.7x on CNN8; under macro-level parallelism, EDAP falls about 70%, 68%, and 36% on the three models.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Run evidence

- The upstream minimal example was actually run (2026-11-04): `TetrisG_SDK.py` finished instantly, exit 0, input cnn8-3, group 2, output VW-SDK 48, optimal PW shape 8x4x16x42, 16 windows, grouped Total CC 32.0. Evidence: [runs/tetrisg-20261104/](../../runs/tetrisg-20261104/). This proves only that the TetrisG script runs one configuration here and outputs window and cycle numbers, not any JETCAS 2026 paper speedups, and it is not a silicon measurement; the NeuroSim C++ part was not built or run.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
