# PIMeval-PIMbench 2026 扩展：面向数字 DRAM PIM 的建模与基准扩展

## 原文信息

- 原文标题：Characterizing Digital DRAM PIM through Modeling and Benchmarking (PIMeval-PIMbench extension, TACO 2026)
- 中文标题：PIMeval-PIMbench 2026 扩展：面向数字 DRAM PIM 的建模与基准扩展
- 作者：Farzana Ahmed Siddique 等（以原文作者表为准）
- 年份与发表处：ACM TACO，2026
- arXiv / DOI：以原文为准

## 核心方法

- 扩展 PIMeval/PIMbench：支持更广的工作负载、PIM 架构与 DRAM 技术，覆盖子阵列级位串行、子阵列级位并行、bank 级位并行三类数字 PIM；加入 roofline 分析与核内执行阶段拆分，找出 PIM 与 CPU/GPU 的交叉点；并分析 DDR/HBM、GDL 宽度等 DRAM 变体的影响。

## 核心效果

- 论文报告（以原文为准）：论文报告：以系统方法给出三类数字 PIM 的适用区间与交叉点，而非单一加速比；具体模型与基准数字以原文表为准，本目录不把骨架的 roofline 斜率当作原文结果。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
