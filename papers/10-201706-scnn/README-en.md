# SCNN: An Accelerator for Compressed-Sparse Convolutional Neural Networks

## Original paper information

- Original title: SCNN: An Accelerator for Compressed-Sparse Convolutional Neural Networks
- Authors: Angshuman Parashar, Minsoo Rhu, Anurag Mukkara, et al.
- Year and venue: 2017, ISCA 2017

## Core method

- Exploit weight sparsity and activation sparsity together: traditional dense accelerators also multiply zero values, while SCNN only performs effective computation on nonzero weights and nonzero activations, skipping the rest.
- Compressed representation: weights and activations are both stored and transferred in compressed formats, reducing on-chip/off-chip data volume; during computation, coordinate information is used to restore the positions of nonzero elements, followed by multiply-accumulate.
- Core hardware structure: a multiplier array + a scatter accumulator array. Product results land at irregular positions, and the scatter accumulator is responsible for accumulating them correctly to the corresponding output positions while maintaining high parallelism.
- The post-processing unit (PPU) handles nonlinearity, pooling, and output compression, ensuring output activations still enter the next layer in compressed form, forming a sparse closed loop across layers.

## Core results

- Representative conclusions reported in the paper (see the original paper for the exact figures): versus a dense convolutional accelerator, SCNN improves performance by about 2.7x and energy efficiency by about 2.3x; exact multiples vary with network sparsity, and higher sparsity gives larger gains.
- Baselines must be distinguished: the paper compares both a traditional dense accelerator (DCNN) and an optimized dense accelerator (DCNN-opt), and multiples differ by baseline, so any citation must state the baseline.
- On low-density layers, speedups can rise further; but irregular accumulation and load imbalance caused by sparsity are also costs SCNN must solve, and peak multiples alone should not be quoted.

## Reproduction points

- Reproduction goal: implement compressed sparse convolution: multiply only nonzero weights and nonzero activations, use scatter accumulation to accumulate results to the correct output positions, and compare MAC counts with dense convolution.
- Measure: sparsity, proportion of MACs skipped, scatter-accumulation conflicts/load imbalance, and speedup curves at different sparsity levels.
- What will not match the original chip: real PE-array timing, HLS-synthesized area and power, and on-chip network congestion; the skeleton only verifies sparse computation correctness and savings.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
