# MICSim：面向混合信号存算一体 AI 加速器的模块化仿真器

## 原文信息

- 原文标题：MICSim: A Modular Simulator for Mixed-signal Compute-in-Memory based AI Accelerator
- 中文标题：MICSim：面向混合信号存算一体 AI 加速器的模块化仿真器
- 作者：Cong Wang、Zeming Chen、Shanshi Huang
- 年份与发表处：ASP-DAC 2025（2025-01-20），541–547 页
- arXiv / DOI：arXiv:2409.14838；DOI 10.1145/3658617.3697630

## 核心方法

- 面向混合信号存算一体（CIM）加速器的模块化电路前仿真器，用于早期评估芯片级软件性能与硬件开销；模块化设计支持多层级协同设计与设计空间探索。
- 由先进的 CIM 仿真器 NeuroSim 模块化而来，提供高度可配置的仿真框架，支持多种量化算法、多种电路/架构设计与不同存储器件，也便于扩展到新设计。
- 原生支持用 Python 评估 CNN 与 Transformer 的软件与硬件性能，基于 PyTorch 与 HuggingFace Transformers；量化层（QLinear / QConv）可直接替换标准 PyTorch 层。
- 提出基于统计的平均模式：先对各目标层转储统计数据（如非零激活比、平均电导），再做硬件评估；硬件性能部分用 pybind11 编译 NeuroSim v1.3 后端。

## 核心效果

- 论文报告（以原文为准）：MICSim 易于结合优化策略做设计空间探索，也可用于芯片级 Transformer CIM 加速器评估；统计平均模式比 NeuroSim 快约 9–32 倍——这是工具之间的对比，不是硅片实测，也不是峰值性能。
- 峰值性能：未给出可比的峰值数字。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（量化后精度、输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。MICSim 本身是仿真工具，其输出是模拟器估计，不是硅片实测；硬件性能评估需要 conda 环境并用 pybind11 编译 NeuroSim v1.3 后端（Python 3.8，Ubuntu 20.04）；上游仓库根目录未找到许可证文件，使用前请以仓库自带文件为准。
