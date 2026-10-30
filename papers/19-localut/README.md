# LoCaLUT：面向 DRAM 存内计算的查表推理（容量-计算权衡）

## 原文信息

- 原文标题：LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM
- 中文标题：LoCaLUT：利用容量-计算权衡实现基于查表的 DRAM 存内推理
- 作者：Junguk Hong、Changmin Shin、Sukjin Kim、Si Ung Noh、Taehee Kwon、Seongyeon Park、Hanjun Kim、Youngsok Kim、Jinho Lee（首尔国立大学等）
- 年份与发表处：2026，HPCA 2026；arXiv:2604.04523；HPCA 2026 最佳论文提名（Best Paper Candidate）。注：部分来源将标题简写为 LOCALUT，以论文标题 LoCaLUT 为准。

## 核心方法

- 查表推理：把多个乘加操作打包进一次查表（LUT lookup），用查表替代乘法，把计算换成容量。
- LUT 规范化：消除重复表项，压缩查表体积；配合重排序 LUT，进一步减少冗余。
- LUT 切片流式传输：利用 DRAM 缓存层次结构做切片流式传输，让查表数据流与 DRAM-PIM 的访存结构匹配。
- 真实系统验证：在基于 UPMEM 的真实系统上评估，而非纯仿真。

## 核心效果

- 论文报告（以原文为准）：在不同数值精度与 DNN 模型上，几何平均加速约 1.82 倍。
- 意义：PIM 路线 2026 年的关键进展——它没有假设未来 DRAM 工艺，而是直面“查表虽省算力、却吃容量”的权衡，并在真实 PIM 硬件上证明了这条路走得通。

## 复现要点

- 复现目标：模拟查表打包——多个小乘加用一次查表完成，统计查表体积、去重前后的表项数与计算量。
- 要测量：打包粒度与表项数的关系、规范化去重率、查表次数与乘法次数之比。
- 不会与原文系统一致的地方：真实 UPMEM 编程模型、DRAM 缓存层次、查表硬件；骨架只验证查表等价性与去重逻辑。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是商用 DRAM 的 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
