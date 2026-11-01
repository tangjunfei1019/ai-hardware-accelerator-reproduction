# 对抗存储墙：长上下文智能体大模型推理的优化路径（PLENA）

## 原文信息

- 原文标题：Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference
- 中文标题：对抗存储墙：长上下文智能体大模型推理的优化路径
- 作者：Haoran Wu、Can Xiao、Jiayi Nie、Xuan Guo、Binglei Lou、Jeffrey T. H. Wong、Zhiwen Mo、Cheng Zhang、Przemyslaw Forys、Chengyang Ai、Timi Adeniran、Wayne Luk、Hongxiang Fan、Jianyi Cheng、Timothy M. Jones、Rika Antonova、Robert Mullins、Aaron Zhao（剑桥大学、帝国理工学院等）
- 年份与发表处：2026，ISCA 2026（第 53 届 ISCA 论文集，第 100–115 页）；arXiv:2509.09505

## 核心方法

- 问题重构：智能体推理不同于聊天推理——上下文极长（整页 DOM、长工具调用轨迹），导致带宽墙与容量墙同时出现，片上计算单元长期处于低利用率。
- 系统 PLENA：软硬件协同设计的三条优化路径——（1）面向胖 GEMM（内维 K 很大）的扁平脉动阵列；（2）混合数据类型与精度的非对称量化，兼顾带宽墙与容量墙；（3）原生支持 FlashAttention 的自定义指令集 PLENA_ISA。
- 完整软件栈：自定义 ISA、编译器、事务级（后为周期级仿真表述）模拟器、自动化设计空间探索流程，构成可复用的整套系统而非单点加速器。

## 核心效果

- 论文最新版摘要报告（以原文为准）：在相同乘法器数量与存储配置下，LLaMA 智能体推理中相对 A100 GPU 最高约 2.23 倍吞吐、相对 TPU v6e 最高约 4.70 倍吞吐，能效相对 A100 最高约 4.04 倍。早期版本曾给出最高约 8.5 倍利用率提升等数字，引用时请以最新版为准。
- 意义：2026 年智能体推理成为独立负载类别的标志性论文——它先论证“为什么现有加速器在这类负载上必然低利用率”，再给出三条路径的联合解法。

## 复现要点

- 复现目标：模拟扁平阵列对胖 GEMM 的利用率优势——对比方阵与扁平阵列在 K 远大于 M、N 时的填充/排空开销与利用率。
- 要测量：不同 M、N、K 形状下的利用率、量化前后的字节数、FlashAttention 融合前后的片外流量。
- 不会与原文系统一致的地方：真实 PLENA_ISA、编译器、模拟器与 RTL（论文称将开源，本次核查未找到可验证的仓库链接）；骨架只验证扁平阵列的利用率算术。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是芯片 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
