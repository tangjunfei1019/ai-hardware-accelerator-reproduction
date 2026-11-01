# NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities

## Original paper information

- Original title: NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities
- Authors: James Read, Ming-Yen Lee, Wei-Hsing Huang, Yuan-Chun Luo, Anni Lu, Shimeng Yu
- Year and venue: IEEE TCAD, 2026
- arXiv / DOI: arXiv:2505.02314 (v2, March 2026)

## Core method

- Rebuilds the NeuroSim software backbone: connects a TensorRT post-training quantization flow, supports more networks (including Transformers); uses pre-characterized statistical models for flexible noise injection, making it easy to plug in SPICE or silicon-measured data; extends device support (including emerging non-volatile capacitive memory); and optimizes behavioral simulation, running up to about 6.5x faster than V1.4.

## Core results

- As reported in the paper (see the original): a ViT case study shows ViT is less noise-tolerant and less area-efficient than a CNN of the same scale; a hybrid ACIM / DCIM architecture provides a basis for Transformer workloads. Specific accuracy and PPA numbers follow the original.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
