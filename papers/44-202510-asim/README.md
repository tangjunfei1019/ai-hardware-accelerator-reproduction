# ASiM：面向基于 SRAM 的模拟存算一体电路的推理精度建模与分析

## 原文信息

- 原文标题：ASiM: Modeling and Analyzing Inference Accuracy of SRAM-Based Analog CiM Circuits
- 中文标题：ASiM：面向基于 SRAM 的模拟存算一体电路的推理精度建模与分析
- 作者：Wenlun Zhang、Shimpei Ando、Yung-Chin Chen、Kentaro Yoshioka
- 年份与发表处：IEEE Transactions on Very Large Scale Integration (VLSI) Systems，2025（第 33 卷第 10 期，2838–2851 页）
- arXiv / DOI：arXiv:2411.11022；DOI 10.1109/TVLSI.2025.3605286

## 核心方法

- 面向基于 SRAM 的模拟存算一体（ACiM）系统的推理精度仿真框架：现有仿真工具很少针对 SRAM ACiM，且精度预测不一致，ASiM 提供标准化的、电路感知的评估方法。
- 对电荷域架构中的关键效应做高保真建模：ADC 量化、位并行编码与模拟噪声；支持 CNN 与 ViT 等 Transformer 模型，可扩展到 ImageNet 规模分类。
- 用户可把 ASiM 模块替换进自己的 DNN 模型，所有可配参数集中在 `config.py`；两种模式：Train（训练/微调）与 Simulation（位级仿真），并支持噪声感知训练（trim_noise）得到更鲁棒的模型。
- 探索混合模拟-数字执行与多数表决两种鲁棒性方案；还提供 RRAM 交叉阵列、全权位并行与电流域 SRAM ACiM 等扩展示例。

## 核心效果

- 论文报告（以原文为准）：位并行编码能在精度仅适度下降的前提下提升能效；但即使 1 LSB 的模拟噪声也会显著损害推理性能，尤其在 ImageNet 等复杂任务上；混合模拟-数字执行与多数表决能在不抵消节能收益的前提下提升鲁棒性。
- 上游给出的仿真时间（全量验证集，见原文 README）：ResNet-18/CIFAR-10（W4A4）在 i9-13980HX 上约 6000 秒，在 RTX4080 笔记本上约 230 秒；ViT-B-32/ImageNet（W8A8）在 A6000 上约 19841 秒。
- 峰值性能：未给出可比的峰值数字（本工具以精度为导向）。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（推理精度随噪声与编码方式的变化趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。ASiM 本身是仿真工具，其输出是模拟器估计，不是硅片实测；ResNet-18/CIFAR-10 可在 CPU 上跑，但全量验证集在 i9 上约 6000 秒，轻量测试只能用小子集，ImageNet / ViT 建议用 GPU；预训练权重通过上游 README 的 Google Drive 链接提供。
