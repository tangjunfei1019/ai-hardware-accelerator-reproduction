# OpenACM：开源 SRAM 近似数字存内计算编译器

## 原文信息

- 原文标题：OpenACM: An Open-Source SRAM-Based Approximate CiM Compiler
- 中文标题：OpenACM：开源 SRAM 近似数字存内计算编译器
- 作者：Yiqi Zhou、JunHao Ma、Xingyang Li、Yule Sheng、Yue Yuan、Yikai Wang、Bochang Wang、Yiheng Wu、Shan Shen、Wei Xing、Daying Sun、Li Li、Zhiqiang Xiao
- 年份与发表处：DATE 2026
- arXiv / DOI：arXiv:2601.11292

## 核心方法

- 把近似计算系统地引入 SRAM 数字 CIM 编译：提供精确、可调近似与对数三类乘法器库，在应用容错范围内做精度-能量权衡；编译器自动生成 DCIM 架构，并把晶体管级可定制 SRAM 宏与变异感知表征接入基于 OpenROAD 与 FreePDK45 的完整物理流程。

## 核心效果

- 论文报告（以原文为准）：论文报告：代表性 CNN 上节能最高约 64%，应用精度损失可忽略；具体模型与近似配置以原文为准。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 运行证据

- 最小前端生成器已实际运行（2026-11-05）：8 位乘法器生成了 `Exact_8bit.v`、`Appro4_2_8bit.v`、`Log_our_8bit.v` 三个 RTL 文件；8 位 / 16 深 SRAM 步骤退出码为 0，但未产生改动，因为上游自带的 `sram.v` 本身已是 16×8 模块。证据见 [runs/openacm-20261105/](../../runs/openacm-20261105/)。这只证明当前 v2 前端能生成 8 位乘法器 RTL，不复现 DATE 2026 的论文数字，也不是芯片实测；PE 与后端流程未尝试。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
