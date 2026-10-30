# DCC：面向存内处理架构的数据中心机器学习内核编译器

## 原文信息

- 原文标题：DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures
- 中文标题：DCC：面向存内处理架构的数据中心机器学习内核编译器
- 作者：Peiming Yang、Sankeerth Durvasula、Ivan Fernandez、Mohammad Sadrosadati、Onur Mutlu、Gennady Pekhimenko、Christina Giannoula
- 年份与发表处：ISCA 2026
- arXiv / DOI：arXiv:2511.15503，10.1109/ISCA66397.2026.00180

## 核心方法

- 提出多层 PIM 抽象，把 PIM 存储层次抽象为 PIM 组，解耦编译器与后端语义；数据中心调度生成器把数据分片策略映射为计算循环分片，联合优化数据重排与计算代码，并用快速性能预测模型选最优配置。

## 核心效果

- 论文报告（以原文为准）：论文报告：相对 GPU 执行，HBM-PIM 上最高约 7.68 倍、平均约 2.7 倍加速，AttAcc 上最高约 13.17 倍、平均约 5.75 倍加速；端到端 LLM 推理在 AttAcc 上最高约 7.71 倍、平均约 4.88 倍加速。演讲幻灯片另给出相对默认实现，单个 ML 内核在 HBM-PIM 约 1.7 倍、AttAcc 约 1.3 倍提升。不同基线不要混用。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
