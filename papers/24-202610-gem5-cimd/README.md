# gem5-CIMD：面向 DRAM 存内计算的全应用 gem5 仿真框架

## 原文信息

- 原文标题：A gem5-based Simulation Framework for Computing-in-DRAM
- 中文标题：gem5-CIMD：面向 DRAM 存内计算的全应用 gem5 仿真框架
- 作者：Alexander Kusnezoff、João Paulo C. de Lima、Jeronimo Castrillon、Asif Ali Khan
- 年份与发表处：arXiv 2026
- arXiv / DOI：arXiv:2610.08186

## 核心方法

- 把 DRAM 子阵列内计算（CIMD）做到全应用 gem5 仿真：扩展指令集到 16 条，覆盖算术、关系、条件与工具类操作，支持 4 至 64 位；多级大页、CIM 感知分配器与子阵列感知地址映射，保证操作数落在同一子阵列。

## 核心效果

- 论文报告（以原文为准）：论文报告：框架可跑完整应用而非仅 trace 回放，并以端到端 KNN 为案例；具体加速与开销数字以原文为准，本目录不把骨架的位运算速度当作 gem5 仿真结果。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
