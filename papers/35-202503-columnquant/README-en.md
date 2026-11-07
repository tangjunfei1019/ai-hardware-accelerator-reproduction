# ColumnQuant / RUnQuant: Column-Granularity Quantization for Compute-in-Memory Accelerators

## Original paper information

- Repository's paper: Column-wise Quantization of Weights and Partial Sums for Accurate and Efficient Compute-In-Memory Accelerators, DATE 2025, arXiv:2502.07842, by Jiyoon Kim et al.
- Follow-up paper from the same repository (per the SKKU IRIS Lab page): RUnQuant: High-Resolution Weight Quantization via Unanchored Weight Decomposition in Column-wise Granularity for CIM Accelerators, Journal of Systems Architecture, 2026 (published 2026-01-17)
- Upstream repository: https://github.com/jiyoonkm/ColumnQuant

## Core method

- Column-granularity alignment: weights and partial sums are quantized with a consistent scaling factor at the same column granularity, rather than mismatched layer/channel granularities, so that in-array MAC results stay consistent with dequantization.
- Unanchored weight decomposition (RUnQuant): instead of conventional zero-anchored decomposition, weights are decomposed without fixing a zero anchor, increasing the representable quantization levels under low-precision cells and removing the two-stage training process.
- Framework: `SplitConv4Pim_group.py` implements CIM-oriented convolution (splitting weights by bits per cell, weight quantization and partial-sum quantization with LSQ, grouped convolution, row-wise partial-sum quantization), with three layer variants (plain, weight-decomposed, weight-decomposed + improved LSQ for binary RRAM).

## Core results

- Per the RUnQuant SKKU page: up to 4.05% accuracy improvement over existing methods, while keeping dequantization overhead. Per the earlier column-granularity paper's summary abstract: about 0.99%, 2.69% and 1.01% improvement over the best comparable methods on different models (ResNet-20/18 on CIFAR-10/100 and ImageNet). Exact per-model tables are as in the original papers; the numbers here are quoted from those secondary summaries and were not re-measured here.
- Impact: it directly tackles the two costs that dominate analog compute-in-memory practice — ADC overhead and crossbar cell-precision limits — and provides a runnable convolution framework, not just a description of the idea.

## Reproduction points

- Reproduction goal: compute a scaling factor per column, do 3-bit quantization and dequantization, and compare the error of column-granularity quantization with layer-granularity quantization.
- What to measure: quantization error at different granularities; do not treat the skeleton output as the paper's accuracy gains.
- What will not match the original tool: the full PyTorch training flow, the LSQ learning process, and ResNet training accuracy; the skeleton only demonstrates the column-granularity quantization idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas and cannot directly reproduce the paper's accuracy numbers.

## Verification notes for this entry

- The upstream repository was verified to exist via `git ls-remote`; the framework files `SplitConv4Pim_group.py`, `LSQ.py` and `any_quant.py` passed `python3 -m py_compile` syntax checks.
- The full clone list also includes `main.py`, `resnet_quan.py` and `utils.py` (listed by filename only; their contents were not checked item by item here, so check them before an end-to-end reproduction) and a ResNet-20 CIFAR-100 W3A3P3 checkpoint in `legacy/` (`ResNet20_Cifar100_W3A3P3_ckpt.pth`).
- The upstream module was actually run (2026-11-02): a minimal `SplitConv4Pim_group` forward pass finished in ~1.3 s, input (1, 64, 32, 32) → output (1, 64, 32, 32). Evidence: [runs/columnquant-20261102/](../../runs/columnquant-20261102/). This proves only that the module builds and runs a forward pass, not any DATE 2025 accuracy table.
- The weakest completeness point: no licence file or requirements file was found in the repository root; check the authors' / paper's licence terms before redistributing or building a product on it.
