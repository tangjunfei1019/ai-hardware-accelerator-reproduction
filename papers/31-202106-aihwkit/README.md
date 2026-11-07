# AIHWKit：面向模拟交叉阵列的灵活快速 PyTorch 工具包

## 原文信息

- 原文标题：A flexible and fast PyTorch toolkit for simulating training and inference on analog crossbar arrays
- 中文标题：AIHWKit：面向模拟交叉阵列的灵活快速 PyTorch 工具包
- 作者：Malte J. Rasch、Diego Moreda、Tayfun Gokmen、Manuel Le Gallo、Fabio Carta、Cindy Goldberg、Kaoutar El Maghraoui、Abu Sebastian、Vijay Narayanan（IBM Research）
- 年份与发表处：2021，AICAS；arXiv:2104.02184
- 上游仓库：https://github.com/IBM/aihwkit

## 核心方法

- 权重映射为“模拟片（analog tile）”：二维权重矩阵存放在阻变交叉阵列上，输入输出周围建模缩放、ADC/DAC 与噪声等前后处理。
- 提供模拟版 PyTorch 层（线性、1D/2D/3D 卷积、LSTM、序列容器）、模拟优化器（AnalogSGD）以及 Tiki-Taka 等原位算法。
- 器件模型可配置：器件间与周期间变异、阻变响应曲线、权重/输出噪声，以及基于 100 万器件 PCM 芯片实测校准的 PCM 统计模型（据仓库 README）。

## 核心效果

- 论文的贡献是一套工具包，而不是单一加速器设计，因此这里不引用单一加速比作为 headline 数字。论文声称该工具包完全支持 GPU 加速，可以估计未来模拟技术材料特性与非理想性对任意人工神经网络精度的影响；各实验的精度表以原文为准。
- 影响：它是第一个被广泛使用的开放 PyTorch 模拟交叉阵列工具包，让普通深度学习研究者无需自建模拟器即可做模拟交叉阵列训练与推理，并成为模拟 AI 硬件感知训练工作的默认基线。

## 复现要点

- 复现目标：用模拟片跑一个小线性层，比较理想计算与加入噪声、ADC/DAC 量化后的输出差异。
- 要测量：不同噪声水平与量化位数下的输出误差；不要把骨架输出当作原文精度表。
- 不会与原文工具一致的地方：真实的 C++/CUDA 模拟器、PCM 器件统计模型、AnalogSGD 与 Tiki-Taka 的完整训练流程；骨架只演示“权重在阵列上 + 噪声 + 量化”这一核心思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的精度与性能数字。

## 本次核实说明

- 上游仓库经 `git ls-remote` 核实存在；仓库内有 30 个示例、教程笔记本、30 个测试文件与 MIT 许可证，文档见 https://aihwkit.readthedocs.io。
- 上游示例已实际运行（2026-11-01）：`examples/01_simple_layer.py` 在 CPU 上约 10 秒跑完，单层 `AnalogLinear(4, 2)` 训练 100 个 epoch，loss 从 0.379（第 1 epoch）降至 0.0093（第 100 epoch）。证据见 [runs/aihwkit-20261101/](../../runs/aihwkit-20261101/)。这只证明工具链能安装并跑通，不复现 AICAS 2021 的任何具体精度表；安装的 aihwkit 1.2.0 是当前 PyPI 版本，不是 2021 年冻结版本。
