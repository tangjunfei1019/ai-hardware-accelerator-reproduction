# DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning

## Original paper information

- Original title: DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning
- Authors: Tianshi Chen, Zidong Du, Ninghui Sun, et al.
- Year and venue: 2014, ASPLOS 2014 (Best Paper)

## Core method

- Neural network computation is abstracted as dense linear algebra: the neural functional unit (NFU) is a three-stage pipeline of a multiplier tree, an adder tree, and a nonlinear activation, supporting 16-bit fixed-point arithmetic.
- The memory hierarchy is key: the input buffer NBin, output buffer NBout, and weight buffer SB are independent, because inputs, weights, and outputs have different access patterns; tiling then cuts large layers into small tiles that fit in the on-chip buffers, and prefetching hides memory latency.
- Control uses a lean domain-specific instruction set rather than the complex control flow of a general-purpose CPU; the same NFU processes multiple neurons in a time-multiplexed way, keeping area small and making it suitable for embedded scenarios.
- The design goal is not a single peak number, but usable neural-network throughput at small area and low power.

## Core results

- The paper reports order-of-magnitude performance and energy-efficiency improvements over a SIMD baseline; different secondary sources quote different multiples with different bases, so when reproducing, use the experimental tables in the original PDF, and do not directly quote second-hand multiples.
- This skeleton does not reproduce the original absolute area and power numbers, because that would require 65 nm process libraries and a synthesis flow, which a software skeleton cannot provide.
- The key verifiable conclusion is qualitative: tiling + three independent buffer types + a fixed-point NFU can significantly reduce off-chip memory pressure.

## Reproduction points

- Reproduction goal: use tiled matrix multiplication to simulate the NFU's computation and buffer behavior, and compare memory accesses with "no tiling, direct memory access" versus "tiled reuse".
- Measure: MAC count, DRAM reads of weights/activations, the effect of tile size on reuse rate, and the error before and after fixed-point quantization.
- What will not match the original chip: cycle counts, area, power, and real on-chip timing; this skeleton only verifies correctness at the algorithm and dataflow level.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
