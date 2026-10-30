# NeuroSim V1.5：面向存内计算加速器的改进软件基准框架

## 原文信息

- 原文标题：NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities
- 中文标题：NeuroSim V1.5：面向存内计算加速器的改进软件基准框架
- 作者：James Read、Ming-Yen Lee、Wei-Hsing Huang、Yuan-Chun Luo、Anni Lu、Shimeng Yu
- 年份与发表处：IEEE TCAD，2026
- arXiv / DOI：arXiv:2505.02314（v2，2026 年 3 月）

## 核心方法

- 重构 NeuroSim 软件主干：接入 TensorRT 后训练量化流程，支持更多网络（含 Transformer）；用预表征统计模型做灵活噪声注入，便于接入 SPICE 或硅实测数据；扩展器件支持（含新兴非易失电容存储器）；优化行为仿真，运行速度相对 V1.4 最高约 6.5 倍。

## 核心效果

- 论文报告（以原文为准）：论文报告：ViT 案例显示，ViT 相对同规模 CNN 对噪声容忍更低、面积效率更低；混合 ACIM/DCIM 架构为 Transformer 工作负载提供基础。具体精度与 PPA 数字以原文为准。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
