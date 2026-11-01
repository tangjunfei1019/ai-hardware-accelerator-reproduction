# AHASD：面向移动端自适应草稿推测解码的异步异构 NPU-PIM 架构

## 原文信息

- 原文标题：AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices
- 中文标题：AHASD：面向移动端自适应草稿推测解码的异步异构 NPU-PIM 架构
- 作者：Ma Zirui、Fan Zhihua、Li Wenxing、Wu Haibin、Zhang Fulin、Ye Xiaochun、Li Wenming
- 年份与发表处：arXiv 2026
- arXiv / DOI：arXiv:2604.25326

## 核心方法

- 把推测解码拆为任务级异步执行：小草稿模型在 PIM 上起草、大目标模型在单个 NPU 上批量验证；熵-历史感知草稿控制与时间感知预验证控制抑制低置信无效草稿；LPDDR5-PIM 内设注意力算法单元与门控任务调度单元，实现注意力定位与亚微秒任务切换。

## 核心效果

- 论文报告（以原文为准）：论文报告：相对 GPU 基线，吞吐最高约 4.2 倍、能效最高约 5.6 倍；相对 GPU+PIM 基线，吞吐约 1.5 倍、能效约 1.24 倍；硬件开销低于 DRAM 面积的 3%。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
