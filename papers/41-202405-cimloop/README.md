# CiMLoop：灵活、准确、快速的存算一体建模工具

## 原文信息

- 原文标题：CiMLoop: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool
- 中文标题：CiMLoop：灵活、准确、快速的存算一体建模工具
- 作者：Tanner Andrulis、Joel S. Emer、Vivienne Sze
- 年份与发表处：ISPASS 2024（2024-05-05），最佳论文奖
- arXiv / DOI：arXiv:2405.07259；DOI 10.1109/ISPASS61541.2024.00012

## 核心方法

- 面向存算一体（CiM）全栈的建模工具，建立在 Timeloop + Accelergy v4 之上：用一套灵活规约描述工作负载并映射到电路与架构，覆盖器件、电路、架构、工作负载与映射多个层级，而不是只看某一级或某一个设计点。
- 准确的能量模型：捕捉深度神经网络操作数值、硬件数据表示与电路传播的模拟/数字值之间的相互作用。
- 快速的统计模型：比其他高精度模型快数个量级，可快速探索协同设计空间；仓库提供教程、示例与可复现论文结果的 notebook（Docker 容器内运行）。
- 使用前提：先完成 Timeloop 与 Accelergy 的教程；论文结果通过运行 `models/arch/1_macro/*/_guide.ipynb` 与 `tutorials/demo_speed_accuracy.ipynb` 复现。

## 核心效果

- 论文报告（以原文为准）：研究者可以在不同层级评估设计选择、跨全栈协同设计、公平比较不同实现，并快速探索设计空间；本文不把骨架的能量估算当作原文结果。
- 峰值性能：未给出可比的峰值数字（统计模型“快数个量级”是相对说法，不是峰值）。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。CiMLoop 本身是建模工具，其输出是模型估算，不是硅片实测；上游仓库已声明停止维护，模型已迁移至 AccelForge / HWComponents，旧仓库仅作归档复现用，今后工作请用 AccelForge 与 HWComponents。
