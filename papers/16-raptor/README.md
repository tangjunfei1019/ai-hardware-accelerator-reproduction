# Raptor：首款 3D-DRAM 生成式推理加速器（早期硅片）

## 原文信息

- 原文标题：Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference
- 中文标题：Raptor 早期硅片：首款面向生成式推理的 3D-DRAM 加速器
- 作者：Prashant J. Nair、Ramyad Hadidi、Subramani Ganesh、Sangamesh Kodge 等（d-Matrix、英属哥伦比亚大学）
- 年份与发表处：2026，ISCA 2026

## 核心方法

- 3D 集成：逻辑 die 与定制 DRAM die 面对面键合，把计算贴到存储上，而不是让 KV 缓存与权重跨越封装边界反复搬运。
- 面向生成式推理的数据流：针对 KV 缓存流做 stream-blocking 等优化，让长上下文推理的访存模式与 3D-DRAM 的带宽结构匹配。
- 目标：用“带宽密度 + I/O 能效”换生成式推理吞吐，而不是单纯堆算力。

## 核心效果

- 论文与相关报道给出的数字（以原文为准，部分吞吐对比为建模型而非量产实测，引用时请注意这一限定）：单卡带宽超过 100 TB/s，I/O 能效约 0.37 pJ/bit；相对基于 HBM 的设计单卡吞吐约 4.71 倍，相对基于 SRAM 的设计约 2.44 倍。
- 意义：2026 年“存算一体”从 2D 走向 3D 封装的标志性工业证据——当 KV 缓存成为主导成本时，封装与存储工艺本身就成了架构。

## 复现要点

- 复现目标：模拟权重/KV 从 HBM（高延迟、低带宽密度）与 3D-DRAM（高带宽密度、低 I/O 能效）两种路径读取时的解码时间与能耗量级。
- 要测量：不同带宽与 pJ/bit 下的解码时间、I/O 能耗、带宽受限程度。
- 不会与原文芯片一致的地方：真实 3D 键合工艺、DRAM die 定制电路、早期硅片实测条件；骨架只验证带宽与能效的算术关系。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是芯片 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
