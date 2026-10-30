# DRAMatic：面向同态加密运算的 UPMEM 存内处理加速

## 原文信息

- 原文标题：DRAMatic Speedup: Accelerating HE Operations on a Processing-in-Memory System
- 中文标题：DRAMatic：面向同态加密运算的 UPMEM 存内处理加速
- 作者：Niklas Klinger、Jonas Sander、Peterson Yuhala、Pascal Felber、Thomas Eisenbarth
- 年份与发表处：arXiv 2026
- arXiv / DOI：arXiv:2602.12433

## 核心方法

- 在 UPMEM 通用 PIM 上实现同态加密基础运算：用剩余数系统（RNS）与数论变换（NTT）优化多项式运算，避开 DPU 弱乘法与昂贵的核间通信，支持安全评估所需的大参数；并首次给出该类负载的 UPMEM 功耗测量。

## 核心效果

- 论文报告（以原文为准）：论文报告：相对此前 UPMEM 上的同态加密实现加速约 334 倍；相对 Microsoft SEAL 显著缩小差距，但仍受数据传输开销与 DPU 乘法性能约束。具体以原文为准。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
