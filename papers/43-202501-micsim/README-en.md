# MICSim: A Modular Simulator for Mixed-signal Compute-in-Memory based AI Accelerator

## Original paper information

- Original title: MICSim: A Modular Simulator for Mixed-signal Compute-in-Memory based AI Accelerator
- Authors: Cong Wang, Zeming Chen, Shanshi Huang
- Year and venue: ASP-DAC 2025 (2025-01-20), pp. 541–547
- arXiv / DOI: arXiv:2409.14838; DOI 10.1145/3658617.3697630

## Core method

- A modular pre-circuit simulator for mixed-signal compute-in-memory (CIM) accelerators, for early-stage evaluation of chip-level software performance and hardware overhead; its modular design supports multi-level co-design and design space exploration.
- Modularized from the state-of-the-art CIM simulator NeuroSim, it provides a highly configurable simulation framework supporting multiple quantization algorithms, diverse circuit / architecture designs, and different memory devices, and it can be extended to new designs.
- It natively evaluates software and hardware performance of CNNs and Transformers in Python, built on PyTorch and HuggingFace Transformers; quantized layers (QLinear / QConv) directly replace standard PyTorch layers.
- It introduces a statistic-based average mode: per-layer statistics (e.g. non-zero activation ratio, average conductance) are dumped first, then used for hardware evaluation; the hardware-performance part compiles the NeuroSim v1.3 backend with pybind11.

## Core results

- As reported in the paper (see the original): MICSim combines easily with optimization strategies for design space exploration and can evaluate chip-level Transformer CIM accelerators; the statistic-based average mode is about 9–32× faster than NeuroSim — a comparison between tools, not a silicon measurement and not a peak performance number.
- Peak performance: no comparable peak number is given.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (post-quantization accuracy, output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers. MICSim itself is a simulation tool, and its outputs are simulator estimates, not silicon measurements; hardware-performance evaluation needs a conda environment and a pybind11 build of the NeuroSim v1.3 backend (Python 3.8, Ubuntu 20.04); and no LICENSE file was found in the upstream repository root, so check the repository's own files before use.
