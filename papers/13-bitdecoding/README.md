# BitDecoding：用张量核心解锁长上下文低比特 KV 缓存解码

## 原文信息

- 原文标题：BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache
- 中文标题：BitDecoding：用张量核心解锁长上下文大模型的低比特 KV 缓存解码
- 作者：Dayou Du、Shijie Cao、Jianyi Cheng、Luo Mai、Ting Cao、Mao Yang（爱丁堡大学、微软研究院等）
- 年份与发表处：2026，HPCA 2026；arXiv:2503.18773（2026 年 1 月修订版 v3）

## 核心方法

- 问题：低比特 KV 缓存能省显存，但已有系统只用 CUDA 核心解码，浪费了 GPU 上算力占主导的张量核心。
- 协同执行：CUDA 核心与张量核心协同解码低比特 KV 缓存，包括张量核心友好的数据布局、warp 级反量化并行、查询变换、张量级与通道级量化、支持混合精度的软件流水线反量化核。
- 架构感知优化：利用 Hopper 的 warpgroup 张量指令与 Blackwell 的 NVFP4 / MXFP4 张量格式。

## 核心效果

- 论文报告（以原文摘要为准）：相对 FP16 FlashDecoding-v2 平均约 7.5 倍解码加速，Blackwell + NVFP4 最高约 8.6 倍，相对已有最优方法最高约 4.3 倍；LLaMA-3.1-8B、128K 上下文下单批解码延迟降低约 3 倍。
- 意义：2026 年长上下文推理的关键矛盾是 KV 缓存带宽，BitDecoding 证明“低比特 KV”只有配上张量核心友好的执行方式才能真正兑现加速。

## 复现要点

- 复现目标：模拟 4 比特 KV 量化与反量化，比较“逐元素反量化后做注意力”与“分块反量化 + 矩阵乘”两种路径的访存量与计算量量级。
- 要测量：不同位宽下的 KV 缓存字节数、反量化开销占比、量化误差。
- 不会与原文系统一致的地方：真实 CUDA / 张量核心核函数、warpgroup 调度、Hopper / Blackwell 硬件实测性能；骨架只验证量化逻辑与访存量算术。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是芯片 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
