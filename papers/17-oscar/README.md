# OSCAR：开源分层 AI 加速器生成器（含精确功耗模型）

## 原文信息

- 原文标题：OSCAR: An Open-Source Flexible and Hierarchical AI Accelerator Generator with Accurate Power Model
- 中文标题：OSCAR：开源灵活分层 AI 加速器生成器与精确功耗模型
- 作者：Jay Zhe-An Mok、Qijun Zhang、Di Pang、Xuejiao Liu、Yao Lu、Dongbo Wang、Zhiyao Xie（香港科技大学等）
- 年份与发表处：2026，ACM Transactions on Design Automation of Electronic Systems（TODAES），2026 年 9 月；DOI: 10.1145/3841479

## 核心方法

- 生成器而非单一加速器：给定硬件与负载规格，自动生成定制 AI 芯片的 Chisel 代码与可综合 RTL，覆盖稠密、Transformer、Winograd、脉动阵列、可重构等多种架构形态。
- 分层灵活设计空间：芯片结构、软件栈与硬件栈按层次组织，设计者可以在同一框架内探索不同层次的取舍。
- 架构级功耗模型：不需要跑完综合就能在早期估计功耗，让设计空间探索不必每次都付出综合代价。

## 核心效果

- 论文报告（以原文为准）：功耗模型相对综合后功耗的误差约 3.8%，相关系数 R 大于 0.99。
- 意义：这是本次补充中“RTL 真正开源”最扎实的代表——它回答的不是“某个加速器有多快”，而是“如何让更多人低成本地生成自己的加速器”。

## 复现要点

- 复现目标：模拟生成器式配置——用一份结构化配置（阵列规模、数据类型、架构风格）生成对应的硬件参数摘要与功耗估计，并检查配置合法性。
- 要测量：不同配置下的 PE 数、片上存储量级、功耗估计变化趋势。
- 不会与原文工具一致的地方：真实 Chisel 生成、综合流程、功耗模型拟合；骨架只演示“配置驱动生成”的思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的功耗模型精度。
