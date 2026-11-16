# PIMSIM-NN: An ISA-based Simulation Framework for Processing-in-Memory Accelerators

## Original paper information

- Original title: PIMSIM-NN: An ISA-based Simulation Framework for Processing-in-Memory Accelerators
- Authors: Xinyu Wang, Xiaotian Sun, Yinhe Han, Xiaoming Chen
- Year and venue: DATE 2024 (2024-03-25, Late Breaking Results)
- arXiv / DOI: arXiv:2402.18089; DOI 10.23919/DATE58400.2024.10546788

## Core method

- Proposes a dedicated instruction set architecture (ISA) for neural networks on processing-in-memory (PIM), a matching compiler, and a cycle-accurate configurable simulator: the compiler turns a neural-network description into an instruction sequence, and the simulator evaluates it under a given architecture configuration, reporting latency, power, and energy.
- The ISA decouples software algorithms from hardware architecture: the same instructions can be evaluated under different architecture configurations, making it easier to compare software and hardware optimizations; the simulator uses event-driven simulation with better support for hardware parallelism.
- The simulator models a chip of many cores connected by a network-on-chip (NoC); each core resembles a RISC processor with four execution units — scalar, vector, matrix, and transfer — where the matrix unit is built from RRAM crossbar arrays and executes matrix-vector multiplication efficiently.
- Simulator inputs are three files: an architecture configuration, a NoC configuration, and a program instruction file; new instructions must be generated from an ONNX model by the pimcomp-nn compiler.

## Core results

- As reported in the paper (see the original): the framework provides an ISA, a compiler, and a cycle-accurate simulator for configurable performance and power evaluation of PIM accelerators; this directory does not treat skeleton instruction counts as paper results.
- The upstream repository's built-in ResNet-18 example reports (simulator estimates, not silicon measurements): about 40 samples/s and 25 ms average latency on a 64-core configuration, with about 59 s of simulator execution time.
- Peak performance: no comparable peak number is given.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers. PIMSIM-NN itself is a simulation tool, and its outputs are simulator estimates, not silicon measurements; new instructions need the pimcomp-nn compiler, and no LICENSE file was found in the upstream repository root, so check the repository's own files before use.
