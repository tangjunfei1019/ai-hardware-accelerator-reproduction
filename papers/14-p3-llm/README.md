# P3-LLM：NPU-PIM 融合的边缘大模型推理加速器

## 原文信息

- 原文标题：P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats
- 中文标题：P3-LLM：基于混合数值格式的 NPU-PIM 融合边缘大模型推理加速器
- 作者：Yuzong Chen、Chao Fang、Xilai Dai、Yuheng Wu、Thierry Tambe、Marian Verhelst、Mohamed S. Abdelfattah（康奈尔大学、鲁汶大学、斯坦福大学）
- 年份与发表处：2026，ISCA 2026；arXiv:2511.06838

## 核心方法

- 异构分工：NPU 负责计算密集的 prefill GEMM，DRAM 存内计算（PIM）负责访存受限的解码，两者集成在同一边缘推理系统里。
- 混合数值格式：不同操作数用不同格式与精度量化（例如 4 比特权重与 KV 缓存、8 比特激活与注意力分数），在压缩效率与精度损失之间按操作数分别取舍。
- 低精度 PIM 计算单元：格式选择与 PIM 单元协同设计，在同等面积下用低精度单元换取更高计算吞吐，缓解高精度 PIM 单元在 DRAM 工艺下面积与功耗过大的问题。
- 算子融合：通过融合降低运行时反量化的开销，避免量化收益被反量化吃掉。

## 核心效果

- 论文报告（以原文摘要为准）：相对 HBM-PIM、Ecco、Pimba 三类已有大模型加速器，平均分别约 4.9 倍、2.0 倍、3.4 倍加速；量化精度优于已有的 KV 缓存量化与权重-激活量化算法。
- 意义：边缘 LLM 推理同时受算力与带宽约束，P3-LLM 给出了“分工 + 混合精度 + 融合”三者必须联合设计才能成立的完整论证。

## 复现要点

- 复现目标：按操作数分配不同位宽（权重 4 比特、激活 8 比特示意），模拟 prefill 走 GEMM、解码走 PIM 式访存受限路径的分工收益。
- 要测量：混合精度下的模型等效字节数、prefill 与解码的访存/计算比、反量化开销占比。
- 不会与原文芯片一致的地方：真实 DRAM PIM 单元、NPU-PIM 互连、边缘功耗与面积；骨架只验证混合精度分工的算术逻辑。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是芯片 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
