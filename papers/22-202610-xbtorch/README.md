# XBTorch：面向交叉阵列深度学习加速器的统一建模与协同设计框架

## 原文信息

- 原文标题：XBTorch: A Unified Framework for Modeling and Co-Design of Crossbar-Based Deep Learning Accelerators
- 中文标题：XBTorch：面向交叉阵列深度学习加速器的统一建模与协同设计框架
- 作者：Osama Yousuf、Andreu L. Glasmann、Martin Lueker-Boden、Sina Najmaei、Gina C. Adam
- 年份与发表处：APL Machine Learning，2026
- arXiv / DOI：arXiv:2601.07086

## 核心方法

- 在 PyTorch 之上统一建模交叉阵列：权重映射为电导、器件变异与噪声注入、量化与梯度分解；有状态模式做层级映射与推理，无状态模式流式处理 LLM 参数，避免为全部参数建持久阵列实例。

## 核心效果

- 论文报告（以原文为准）：论文报告：框架在器件建模、硬件感知训练与推理容错上与已有工具可比，并在 LLM 无状态评估上可处理大模型；具体精度与加速数字以原文表为准，本目录不把骨架输出当作原文数字。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 运行证据

- 上游最小例子已实际运行（2026-11-04）：README 的两层感知机 `SimpleMLP(10, 5, 2)` 经 `xbtorch_model` 打补丁后一次前向传播约 12 秒跑完，输入 (4, 10) 返回 (4, 2)。证据见 [runs/xbtorch-20261104/](../../runs/xbtorch-20261104/)。这只证明上游模块能构建、打补丁并跑通一次前向传播，不复现 APL Machine Learning 2026 的任何精度表。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
