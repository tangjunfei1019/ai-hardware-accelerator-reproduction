# EIE: Efficient Inference Engine on Compressed Deep Neural Network

## Original paper information

- Original title: EIE: Efficient Inference Engine on Compressed Deep Neural Network
- Authors: Song Han, Xingyu Liu, Huizi Mao, et al.
- Year and venue: 2016, ISCA 2016

## Core method

- Compress first, then accelerate: Deep Compression has three steps — pruning (removing redundant connections), trained quantization (weight sharing, where multiple connections share the same weight value), and Huffman coding — compressing large models so they fit in on-chip SRAM.
- EIE runs inference directly in the compressed format: weights are stored in CSC (compressed sparse column) format, a PE array performs sparse matrix-vector multiplication in parallel, skipping zero weights and zero activations, so no compute or bandwidth is wasted on zero values.
- Key mechanisms: weight sharing (looking up the real weight from a codebook), relative indexing, leading-nonzero detection (finding the next nonzero activation), and each PE storing only one partition of the network, which is naturally parallel.
- The energy savings multiply across layers: SRAM instead of DRAM, sparse skipping, weight sharing, and skipping ReLU zero activations each save a part.

## Core results

- Results reported in the paper (arXiv:1602.01528 abstract, see the original paper for the exact figures): about 102 GOPS on the compressed network, equivalent to about 3 TOPS on the uncompressed network; AlexNet fully-connected layers at about 1.88×10^4 frames/sec, at only about 600 mW.
- Breakdown of gains: DRAM→SRAM about 120x energy saving; sparsity about 10x; weight sharing about 8x; skipping ReLU zero activations about another 3x; versus CPU/GPU, speed about 189x / 13x, and energy efficiency about 24,000x / 3,400x (comparison conditions and baselines as in the original paper).
- Versus DaDianNao, the paper reports about 2.9x throughput, about 19x energy efficiency, and about 3x area efficiency.

## Reproduction points

- Reproduction goal: implement CSC sparse matrix-vector multiplication + a weight-sharing codebook, and verify the MAC savings from skipping zero values and accuracy retention (on a small model).
- Measure: pruning rate, quantization codebook size, proportion of MACs skipped, accuracy change before and after quantization, and SRAM capacity required.
- What will not match the original chip: real PE-array timing, 45 nm/28 nm power, and Huffman decoding hardware; the skeleton only verifies the correctness of the algorithm and sparse computation.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
