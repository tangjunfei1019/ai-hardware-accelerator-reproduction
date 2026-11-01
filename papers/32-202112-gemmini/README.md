# Gemmini：敏捷脉动阵列生成器

## 原文信息

- 原文标题：Gemmini: An Agile Systolic Array Generator Enabling Systematic Evaluations of Deep-Learning Architectures
- 中文标题：Gemmini：敏捷脉动阵列生成器
- 作者：Hasan Genc、Ameer Haj-Ali、Vighnesh Iyer、Alon Amid、Howard Mao、John Wright、Colin Schmidt、Jerry Zhao、Albert Ou、Max Banister、Yakun Sophia Shao、Borivoje Nikolic、Ion Stoica、Krste Asanovic（UC Berkeley）
- 年份与发表处：arXiv:1911.09925（2019，2021 年修订）；完整系统版见 DAC 2021
- 上游仓库：https://github.com/ucb-bar/gemmini

## 核心方法

- Chisel 生成器：生成脉动阵列加速器（矩阵乘法，外加激活、池化、im2col 等深度学习推理辅助功能），与 Rocket Chip SoC 生成器集成，主机可用 Rocket 顺序核或 BOOM 乱序核。
- 支持输出平稳与权重平稳两种数据流、多种数据类型，以及完整软件栈（`libgemmini`），同一设计可在系统级评估，而不只是孤立阵列。
- 论文评估使用 FireSim（FPGA 加速的周期精确仿真）做设计空间探索；所选设计点相对主机处理器在边缘深度学习推理上达到两到三个数量级的加速（论文报告范围，具体设计点以原文为准）。

## 核心效果

- 影响：Gemmini 把深度学习加速器设计从一次性 RTL 工程变成了可参数化生成器——脉动阵列规模、数据流、数据类型与存储层次都可在配置中改动，并成为 RISC-V Chipyard 生态中的标准开放基线，包括 TSMC 16nm 与 Intel 22FFL 的流片测试芯片。
- 这里不把 100–1000 倍范围当作单一“结果”引用，因为结果取决于所选配置；确切数字见论文的设计空间探索案例。

## 复现要点

- 复现目标：用分块（tiling）模拟脉动阵列的矩阵乘法，理解输出平稳数据流下权重/输入/部分和如何在阵列中流动。
- 要测量：不同分块尺寸下的有效乘法次数与数据复用趋势。
- 不会与原文工具一致的地方：真实 Chisel 生成、Verilator 周期仿真、FireSim FPGA 仿真、综合面积与功耗；骨架只演示分块矩阵乘的思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。

## 本次核实说明

- 上游仓库经 `git ls-remote` 核实存在；仓库内有 Chisel RTL 生成器（`src/`，数得 61 个 Scala 文件）、软件栈、建模目录与测试。
- 本次未端到端构建上游，原因是 Chipyard/Spike/Verilator 从头构建是多小时的工具链工作，未尝试；仓库结构、README 快速入门、软件测试与 Chisel 源码已核实存在。
