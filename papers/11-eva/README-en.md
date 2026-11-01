# EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture

## Original paper information

- Original title: EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture
- Authors: Bowen Duan, Cong Guo, Chiyue Wei, Haoxuan Shan, Yuzhe Fu, Xinhua Chen, Yifan Xu, Ziyue Zhang, Changchun Zhou, Hai Li, Yiran Chen (Duke University)
- Year and venue: 2026, ISCA 2026; arXiv:2605.24144

## Core method

- Weight vector quantization: weight matrices are grouped into vectors and clustered into a shared codebook, so weights are stored only as low-precision indices, reaching roughly 2-bit-level weight compression.
- Key insight: decoding is a memory-bound small GEMV. Instead of dequantizing the quantized weights first, EVA computes the dot product of the input vector directly with the weight codebook, turning decoding from a GEMV form into a GEMM-like compute form.
- Conflict-free structured lookup: combining input-codebook computation with a conflict-free memory-access design to solve the bank-conflict problem common in lookup architectures.
- Hardware-software co-design: the architecture is specialized for decoding while remaining compatible with regular prefill execution, rather than being an isolated decoding-only module.

## Core results

- As reported in the paper (see the original abstract): up to about 11.17x speedup and about 7.17x energy-efficiency improvement over the best lookup architecture at the time, while preserving arithmetic precision after vector quantization.
- Significance: it turns "quantization compression" from merely saving memory into an architectural opportunity that "changes the compute form" — one of the most direct examples in 2026 of quantization combined with architecture for decoding acceleration.

## Reproduction points

- Reproduction goal: build a small codebook and weight indices, and compare the two paths — "dequantize first, then multiply-accumulate" versus "input x codebook dot product, then sum by index" — for result consistency and memory-access differences.
- Measure: how codebook size and index bit-width affect the compression ratio, the multiply-accumulate and lookup counts of the two paths, and the quantization error.
- What will not match the original chip: real codebook learning (cluster training), conflict-free memory-access hardware, the on-chip memory hierarchy, and clock/power numbers; the skeleton only verifies computational equivalence.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
