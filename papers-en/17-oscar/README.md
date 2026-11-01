# OSCAR: An Open-Source Flexible and Hierarchical AI Accelerator Generator with Accurate Power Model

## Original paper information

- Original title: OSCAR: An Open-Source Flexible and Hierarchical AI Accelerator Generator with Accurate Power Model
- Authors: Jay Zhe-An Mok, Qijun Zhang, Di Pang, Xuejiao Liu, Yao Lu, Dongbo Wang, Zhiyao Xie (Hong Kong University of Science and Technology, and others)
- Year and venue: 2026, ACM Transactions on Design Automation of Electronic Systems (TODAES), September 2026; DOI: 10.1145/3841479

## Core method

- A generator, not a single accelerator: given hardware and workload specifications, it automatically generates Chisel code and synthesizable RTL for a custom AI chip, covering dense, Transformer, Winograd, systolic-array, reconfigurable, and other architecture forms.
- Hierarchical flexible design space: chip structure, software stack, and hardware stack are organized by level, so designers can explore trade-offs at different levels within the same framework.
- Architecture-level power model: power can be estimated early without running full synthesis, so design-space exploration does not pay the synthesis cost every time.

## Core results

- As reported in the paper (see the original): the power model error is about 3.8% relative to post-synthesis power, with correlation coefficient R greater than 0.99.
- Significance: the strongest "RTL truly open source" representative in this supplement — it answers not "how fast is one accelerator", but "how can more people generate their own accelerator at low cost".

## Reproduction points

- Reproduction goal: simulate generator-style configuration — use a structured configuration (array size, data type, architecture style) to produce a corresponding hardware parameter summary and power estimate, and check configuration validity.
- Measure: PE counts, on-chip memory magnitude, and power-estimate trends under different configurations.
- What will not match the original tool: real Chisel generation, the synthesis flow, and power-model fitting; the skeleton only demonstrates the "configuration-driven generation" idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original power-model accuracy.
