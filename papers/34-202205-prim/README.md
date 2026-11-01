# PrIM：面向真实存内处理系统的首个基准测试集

## 原文信息

- 原文标题：Benchmarking a New Paradigm: Experimental Analysis and Characterization of a Real Processing-in-Memory System
- 中文标题：PrIM：面向真实存内处理系统的首个基准测试集
- 作者：Juan Gómez-Luna、Izzat El Hajj、Ivan Fernandez、Christina Giannoula、Geraldo F. Oliveira、Onur Mutlu
- 年份与发表处：2022，IEEE Access（DOI: 10.1109/ACCESS.2022.3174101）；arXiv:2105.03814
- 上游仓库：https://github.com/CMU-SAFARI/prim-benchmarks

## 核心方法

- 先用微基准刻画 UPMEM 系统（每个 DRAM bank 旁有通用顺序核，称 DPU）的计算吞吐与访存带宽，再在真实 UPMEM 系统（论文中为 640 与 2556 个 DPU）上跑 PrIM 的 16 个负载，并与 CPU/GPU 对照。
- 每个基准都包含主机代码、DPU 代码（`dpu/task.c`）、支撑代码与 CPU/GPU 基线，仓库根目录还有 `run_strong_full.py`、`run_strong_rank.py` 与 `run_weak.py` 扩展性脚本。
- 论文的结论是编程建议（哪些负载适合 PIM、如何跨 DPU 分区），而不是单一加速器设计。

## 核心效果

- 影响：PrIM 是第一个面向第一个公开可用的真实 PIM 硬件（UPMEM）的基准测试集，成为后来 PIM 论文共同比较的标尺——16 个负载覆盖线性代数、数据库、图处理、神经网络、生物信息与图像处理，外加架构极限微基准。
- 论文结果是各负载在两套真实 UPMEM 系统上的扩展性与性能/能效对比表，见 IEEE Access 原文；这里不引用单一加速比作为 headline，因为 PrIM 是基准集，不是单个核。

## 复现要点

- 复现目标：先跑 CPU 基线理解基准，再理解 DPU 分区：把向量按 DPU 数量切分，每核算一段，最后汇总。
- 要测量：不同元素数量与分区数下的基线耗时趋势。
- 不会与原文工具一致的地方：真实 DPU 上的核时间与能效、扩展性曲线；骨架只演示分区思想，CPU 基线结果见 CODE.md。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的 DPU 性能数字。

## 本次核实说明

- 上游仓库经 `git ls-remote` 核实存在；仓库内有 16 个基准目录与微基准，每个基准含主机 + DPU + 支撑代码。
- CPU 基线已实际运行：`VA/baselines/cpu` 用 `gcc -fopenmp` 编译并运行，输出 `nr_elements 16777216，Kernel Time (ms): 59.957000`。这是 CPU 基线，不是 DPU 结果。
- 完整 DPU 结果未运行，原因是该虚拟机没有 UPMEM 硬件与 SDK。
