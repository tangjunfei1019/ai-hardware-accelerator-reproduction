# Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference (PLENA)

## Original paper information

- Original title: Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference
- Authors: Haoran Wu, Can Xiao, Jiayi Nie, Xuan Guo, Binglei Lou, Jeffrey T. H. Wong, Zhiwen Mo, Cheng Zhang, Przemyslaw Forys, Chengyang Ai, Timi Adeniran, Wayne Luk, Hongxiang Fan, Jianyi Cheng, Timothy M. Jones, Rika Antonova, Robert Mullins, Aaron Zhao (University of Cambridge, Imperial College London, and others)
- Year and venue: 2026, ISCA 2026 (53rd ISCA proceedings, pages 100–115); arXiv:2509.09505

## Core method

- Problem reframing: agentic inference differs from chat inference — contexts are extremely long (whole-page DOMs, long tool-call traces), so the bandwidth wall and the capacity wall appear together, leaving on-chip compute units chronically underutilized.
- System PLENA: a hardware-software co-designed set of three optimization paths — (1) a flat systolic array for fat GEMMs (with very large inner dimension K); (2) asymmetric quantization with mixed data types and precisions, addressing both the bandwidth wall and the capacity wall; (3) the custom instruction set PLENA_ISA with native FlashAttention support.
- Full software stack: custom ISA, compiler, transaction-level (later described as cycle-level) simulator, and an automated design-space exploration flow — a reusable complete system, not a single-point accelerator.

## Core results

- As reported in the latest version of the paper abstract (see the original): at the same multiplier count and memory configuration, up to about 2.23x throughput over an A100 GPU and up to about 4.70x over a TPU v6e in LLaMA agentic inference, and up to about 4.04x energy efficiency over an A100. An earlier version gave figures such as up to about 8.5x utilization improvement — cite the latest version.
- Significance: a landmark paper marking agentic inference as an independent workload class in 2026 — it first argues "why existing accelerators must be underutilized on this workload", then gives the joint solution of the three paths.

## Reproduction points

- Reproduction goal: simulate the flat array's utilization advantage on fat GEMMs — compare square versus flat arrays on fill/drain overhead and utilization when K is much larger than M and N.
- Measure: utilization under different M, N, K shapes, byte counts before and after quantization, and off-chip traffic before and after FlashAttention fusion.
- What will not match the original system: the real PLENA_ISA, compiler, simulator, and RTL (the paper says they will be open sourced; no verifiable repository link was found in this check); the skeleton only verifies the flat-array utilization arithmetic.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
