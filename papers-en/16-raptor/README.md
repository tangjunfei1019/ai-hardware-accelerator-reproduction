# Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference

## Original paper information

- Original title: Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference
- Authors: Prashant J. Nair, Ramyad Hadidi, Subramani Ganesh, Sangamesh Kodge, et al. (d-Matrix, University of British Columbia)
- Year and venue: 2026, ISCA 2026

## Core method

- 3D integration: a logic die face-to-face bonded with a custom DRAM die, putting compute next to memory instead of moving KV cache and weights repeatedly across the package boundary.
- Dataflow for generative inference: optimizations such as stream-blocking for the KV-cache stream, matching long-context inference memory patterns to the bandwidth structure of 3D-DRAM.
- Goal: trade "bandwidth density + I/O energy efficiency" for generative inference throughput, rather than simply stacking more compute.

## Core results

- Figures given in the paper and related reports (see the original; some throughput comparisons are modeled rather than production measurements, so note that qualification when citing): single-card bandwidth over 100 TB/s, I/O energy efficiency about 0.37 pJ/bit; about 4.71x single-card throughput over HBM-based designs and about 2.44x over SRAM-based designs.
- Significance: a landmark industry signal in 2026 for "compute-in-memory" moving from 2D to 3D packaging — when the KV cache becomes the dominant cost, packaging and memory process themselves become architecture.

## Reproduction points

- Reproduction goal: simulate decoding time and energy magnitude when weights/KV are read through an HBM path (higher latency, lower bandwidth density) versus a 3D-DRAM path (higher bandwidth density, lower I/O energy).
- Measure: decoding time, I/O energy, and bandwidth-bound degree under different bandwidths and pJ/bit values.
- What will not match the original chip: real 3D bonding processes, custom DRAM-die circuits, and early-silicon measurement conditions; the skeleton only verifies the bandwidth-and-energy arithmetic.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
