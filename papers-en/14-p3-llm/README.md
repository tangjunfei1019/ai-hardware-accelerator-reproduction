# P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats

## Original paper information

- Original title: P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats
- Authors: Yuzong Chen, Chao Fang, Xilai Dai, Yuheng Wu, Thierry Tambe, Marian Verhelst, Mohamed S. Abdelfattah (Cornell University, KU Leuven, Stanford University)
- Year and venue: 2026, ISCA 2026; arXiv:2511.06838

## Core method

- Heterogeneous division of labor: the NPU handles compute-intensive prefill GEMM, while DRAM processing-in-memory (PIM) handles memory-bound decoding, integrated in the same edge inference system.
- Hybrid numerical formats: different operands use different formats and precisions (for example 4-bit weights and KV cache, 8-bit activations and attention scores), trading compression efficiency against accuracy loss per operand.
- Low-precision PIM compute units: format selection is co-designed with the PIM units, trading lower-precision units for higher compute throughput at the same area, easing the problem that high-precision PIM units are too large and power-hungry in DRAM processes.
- Operator fusion: fusion reduces runtime dequantization overhead, so quantization gains are not eaten up by dequantization.

## Core results

- As reported in the paper (see the original abstract): on average about 4.9x, 2.0x, and 3.4x speedups over HBM-PIM, Ecco, and Pimba LLM accelerators respectively; quantization accuracy is better than existing KV-cache quantization and weight-activation quantization algorithms.
- Significance: edge LLM inference is constrained by both compute and bandwidth, and P3-LLM gives a complete argument that "division of labor + hybrid precision + fusion" must be designed jointly to work.

## Reproduction points

- Reproduction goal: assign different bit-widths per operand (4-bit weights, 8-bit activations in the sketch), and simulate the division-of-labor gain of prefill going through GEMM and decoding going through a PIM-style memory-bound path.
- Measure: equivalent model byte counts under hybrid precision, prefill vs decoding memory/compute ratios, and the share of dequantization overhead.
- What will not match the original chip: real DRAM PIM units, NPU-PIM interconnect, and edge power and area; the skeleton only verifies the hybrid-precision division-of-labor arithmetic.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
