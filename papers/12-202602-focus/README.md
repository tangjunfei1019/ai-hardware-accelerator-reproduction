# Focus：面向视觉语言模型的流式集中架构

## 原文信息

- 原文标题：Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models
- 中文标题：Focus：面向高效视觉语言模型的流式集中架构
- 作者：Chiyue Wei、Cong Guo、Junyao Zhang、Haoxuan Shan、Yifan Xu、Ziyue Zhang、Yudong Liu、Qinsi Wang、Changchun Zhou、Hai Li、Yiran Chen
- 年份与发表处：2026，HPCA 2026；arXiv:2512.14661，DOI: 10.1109/HPCA68181.2026.11408525；HPCA 2026 最佳论文提名（Best Paper Nominee / Candidate）

## 核心方法

- 问题：视觉语言模型的视觉 token 数量大、冗余高，token 全量进入大模型既费算力又费访存。
- 多级流式集中（streaming concentration）：在脉动阵列加速器中作为可组合模块，分三级削减冗余——语义引导的 token 剪枝、时空块级集中、基于运动感知匹配的向量级冗余去除。
- 流式而非离线：集中过程与计算流水线结合，避免先把全部 token 存下来再筛选的额外访存。

## 核心效果

- 论文摘要报告（以原文为准）：约 2.4 倍加速、约 3.3 倍能耗降低；结论部分的细分数字为最高约 2.35 倍加速、约 3.29 倍能效提升，面积开销约 2.7%。
- 意义：2026 年多模态推理的瓶颈从“语言模型本身”扩展到“视觉 token 洪流”，Focus 把 token 压缩做进了加速器数据通路，而不是只留在算法层。

## 复现要点

- 复现目标：模拟三级筛选——按语义分数剪枝、按块聚合、按相似度去重，统计 token 削减率与保留信息的近似程度。
- 要测量：各级削减后的 token 数、剪枝阈值与削减率的关系、去重对后续计算量的影响。
- 不会与原文芯片一致的地方：真实语义分数来源（视觉编码器输出）、运动感知匹配的硬件实现、脉动阵列时序与面积功耗；骨架只验证筛选逻辑与削减量。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是芯片 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
