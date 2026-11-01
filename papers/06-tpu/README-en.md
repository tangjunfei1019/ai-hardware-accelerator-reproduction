# In-Datacenter Performance Analysis of a Tensor Processing Unit

## Original paper information

- Original title: In-Datacenter Performance Analysis of a Tensor Processing Unit
- Authors: Norman P. Jouppi, Cliff Young, Nishant Patil, David Patterson, et al.
- Year and venue: 2017, ISCA 2017

## Core method

- Domain-specific architecture: the TPU's core is a 256×256 8-bit systolic-array matrix-multiply unit, with weights flowing in from one side and activations from the other, and partial sums flowing inside the array, completing a large number of multiply-accumulates in a single cycle.
- Large software-managed on-chip storage: about 28 MiB of on-chip storage (including the unified buffer and accumulators), managed explicitly by software rather than relying on a general-purpose CPU's caches, out-of-order execution, prefetching, and other time-varying optimizations; this is friendlier to the 99th-percentile latency of inference.
- Quantized inference: training in floating point and inference in 8-bit integers, trading controllable accuracy loss for compute density and energy efficiency; the instruction set is CISC-like domain-specific instructions (read host memory, read weights, matrix multiply/convolve, activate, and so on).
- The goal is not general-purpose computing, but 95% of datacenter inference load (MLPs, CNNs, LSTMs), for which generality is sacrificed.

## Core results

- Results reported in the paper (arXiv:1704.04760 abstract, see the original paper for the exact figures): peak about 92 TOPS (8-bit), on-chip storage about 28 MiB; compared with a contemporary Haswell CPU and Nvidia K80 GPU, on average about 15x to 30x faster, with TOPS/W about 30x to 80x higher.
- The bottleneck analysis is equally important: some applications have low utilization and are mostly memory-bound; if the TPU's memory were replaced with the K80's GDDR5, the paper estimates performance and energy efficiency would improve further.
- Latency conclusion: a deterministic execution model is friendlier to inference services' tail latency than the time-varying optimizations of CPUs/GPUs.

## Reproduction points

- Reproduction goal: simulate matrix multiplication with a systolic array, measure how array size, data inflow rhythm, and utilization relate, and verify that "how weights/activations flow determines utilization".
- Measure: PE utilization under different matrix shapes, pipeline fill and drain overhead, and error before and after 8-bit quantization.
- What will not match the original chip: the real TPU clock, power, datacenter deployment conditions, proprietary instructions, and software stack; the skeleton only verifies systolic-array computational correctness and utilization trends.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
