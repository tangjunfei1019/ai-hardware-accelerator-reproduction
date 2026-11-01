# BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache

## Original paper information

- Original title: BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache
- Authors: Dayou Du, Shijie Cao, Jianyi Cheng, Luo Mai, Ting Cao, Mao Yang (University of Edinburgh, Microsoft Research, and others)
- Year and venue: 2026, HPCA 2026; arXiv:2503.18773 (revised v3, January 2026)

## Core method

- Problem: low-bit KV caches save memory, but existing systems decode only with CUDA cores, wasting the tensor cores that dominate GPU compute.
- Co-execution: CUDA cores and tensor cores cooperatively decode the low-bit KV cache, including a tensor-core-friendly data layout, warp-level parallel dequantization, query transformation, tensor-level and channel-level quantization, and a software-pipelined dequantization kernel supporting mixed precision.
- Architecture-aware optimization: uses Hopper warpgroup tensor instructions and Blackwell NVFP4 / MXFP4 tensor formats.

## Core results

- As reported in the paper (see the original abstract): about 7.5x average decoding speedup over FP16 FlashDecoding-v2, up to about 8.6x on Blackwell + NVFP4, and up to about 4.3x over the best prior method; for LLaMA-3.1-8B with a 128K context, single-batch decoding latency falls about 3x.
- Significance: in 2026, the key tension in long-context inference is KV-cache bandwidth, and BitDecoding shows that "low-bit KV" only delivers real speedup when paired with a tensor-core-friendly execution style.

## Reproduction points

- Reproduction goal: simulate 4-bit KV quantization and dequantization, comparing "element-wise dequantize then attend" with "block dequantize + matrix multiply" in terms of memory traffic and compute magnitude.
- Measure: KV-cache byte counts at different bit-widths, the share of dequantization overhead, and the quantization error.
- What will not match the original system: real CUDA / tensor-core kernels, warpgroup scheduling, and Hopper / Blackwell hardware measurements; the skeleton only verifies the quantization logic and memory-traffic arithmetic.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
