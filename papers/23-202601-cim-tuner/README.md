# CIM-Tuner：通过硬件-映射协同探索平衡 SRAM-CIM 计算与存储容量

## 原文信息

- 原文标题：CIM-Tuner: Balancing the Compute and Storage Capacity of SRAM-CIM Accelerator via Hardware-mapping Co-exploration
- 中文标题：CIM-Tuner：通过硬件-映射协同探索平衡 SRAM-CIM 计算与存储容量
- 作者：Jinwu Chen、Yuhui Shi、He Wang、Zhe Jiang、Jun Yang、Xin Si、Zhenhua Zhu
- 年份与发表处：arXiv 2026
- arXiv / DOI：arXiv:2601.18070

## 核心方法

- 用矩阵抽象统一多种 CIM 宏，用通用加速器模板做硬件-映射协同探索：在面积约束下同时搜硬件配置与映射策略，平衡计算容量与存储容量，而不是先定硬件再凑映射。

## 核心效果

- 论文报告（以原文为准）：论文报告：扩展策略空间相对已有 CIM 映射，能效提升约 1.58 倍、吞吐提升约 2.11 倍；同面积预算下对已有 CIM 加速器也有可比提升；论文称仿真精度经硅验证，具体以原文为准。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
