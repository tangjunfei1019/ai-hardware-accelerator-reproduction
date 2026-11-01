# FSGen: Agile Fused and Sparse Accelerator Generator with Accurate Power Model for LLM Applications

## Original paper information

- Original title: FSGen: Agile Fused and Sparse Accelerator Generator with Accurate Power Model for LLM Applications
- Authors: Jay Zhe-An Mok, Qijun Zhang, Zhiyao Xie (Hong Kong University of Science and Technology)
- Year and venue: 2026, DAC 2026 (63rd ACM/IEEE Design Automation Conference, July 2026, Long Beach, USA); DOI: 10.1145/3770743.3804052; arXiv:2608.09252

## Core method

- Fused and sparse dataflow representation: a unified representation describes sparse and fused operators' dataflows, supporting fully configurable fused dataflows and sparsity patterns.
- Chisel RTL generator: RTL is generated directly from a configuration, not just a simulation model; it also provides early machine-learning-based PPA (power / performance / area) estimation.
- For LLMs: fusion (for example fusing attention with surrounding operators) reduces off-chip memory traffic, and sparsity skips zero-valued compute; combined, they serve large-model inference.

## Core results

- As reported in the paper (see the original): about 1.4x power efficiency or about 10x speedup over prior work at similar PPA; another passage gives about 58x figure of merit — cite that number only under the paper's own definition.
- Significance: from the same team as OSCAR's generator line, but FSGen specializes in the LLM combination of "fusion + sparsity" — a representative of 2026 large-model accelerators moving from general GEMM toward operator-level co-design.

## Reproduction points

- Reproduction goal: simulate the joint reduction in memory traffic and compute from fusion (skipping intermediate-result write-back) and sparsity (skipping zero values).
- Measure: off-chip traffic before and after fusion, sparsity versus effective MAC count, and the multiplicative effect of the two.
- What will not match the original tool: real Chisel generation, sparse-encoding hardware, and PPA model fitting; the skeleton only verifies the fusion-and-sparsity gain arithmetic.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original PPA numbers.
