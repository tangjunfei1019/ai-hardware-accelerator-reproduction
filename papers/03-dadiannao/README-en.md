# DaDianNao: A Machine-Learning Supercomputer

## Original paper information

- Original title: DaDianNao: A Machine-Learning Supercomputer
- Authors: Yunji Chen, Tao Luo, Shaoli Liu, et al.
- Year and venue: 2014, MICRO 2014 (Best Paper)

## Core method

- DianNao is scaled from a single chip to multiple chips: multiple compute tiles are organized around on-chip eDRAM, each tile has its own weight storage, and the whole model is kept on chip as much as possible, avoiding repeated trips to off-chip DRAM.
- It exploits the separability of neural network layers: different tiles handle different output neurons / filters, activations are distributed by broadcast, weights stay local, giving good locality and good scalability.
- The storage-to-compute ratio is the design center: rather than adding more multipliers first, put the model into on-chip storage and then talk about compute power; this matters most for large models.
- It likewise uses 16-bit / 32-bit fixed-point, NFU-style compute units, and tiling, but scale and interconnect are the new challenges.

## Core results

- The paper reports: after aggregating on-chip storage across multiple chips, large-model inference is no longer bottlenecked by off-chip bandwidth, with significant speedups over CPU/GPU; exact multiples vary with the model, scale, and baseline, so when reproducing, use the experimental tables in the original PDF — this summary does not carry over second-hand multiples.
- The key conclusion is scalability: as the number of chips grows, on-chip model capacity and compute capability can scale together, rather than hitting a single-chip linear bottleneck.
- Absolute area and power numbers depend on the 28 nm process and eDRAM implementation, and a software skeleton cannot reproduce them.

## Reproduction points

- Reproduction goal: simulate multi-tile partitioning: output channels are assigned to different tiles, weights are stored locally, activations are broadcast, and off-chip accesses are counted as tile count and model size vary.
- Measure: off-chip read volume, broadcast volume, load balance (differences in MAC count across tiles), and the speedup and marginal gain when tile count doubles.
- What will not match the original chip: inter-tile interconnect latency, eDRAM bandwidth and power, and the real clock frequency.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
