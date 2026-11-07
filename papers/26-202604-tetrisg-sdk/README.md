# TetrisG-SDK：面向快速存内计算的自适应窗口与分组卷积映射框架

## 原文信息

- 原文标题：TetrisG-SDK: Efficient Convolutional Layer Mapping with Adaptive Windows and Grouped Convolutions for Fast In-Memory Computing
- 中文标题：TetrisG-SDK：面向快速存内计算的自适应窗口与分组卷积映射框架
- 作者：Ke Dong、Kejie Huang、Tao Luo、Bo Wang
- 年份与发表处：IEEE JETCAS（2026 年接收）
- arXiv / DOI：arXiv:2604.25377

## 核心方法

- 在移位复制核（SDK）映射上引入自适应窗口：窗口可容纳更多输入通道、利用边际空间、适应不同通道深度；再结合分组卷积减少计算周期，同时用已验证的 CIM 硬件仿真器给出延迟、面积与能量估计。

## 核心效果

- 论文报告（以原文为准）：论文报告：相对单宏 VWC-SDK，CNN8、GoogLeNet Inception、DenseNet40 分别加速约 1.2 倍、1.3 倍、1.3 倍；系统级延迟与能量在 CNN8 上分别降低约 2.4 倍与 1.7 倍；宏级并行下 EDAP 在三模型上分别降低约 70%、68%、36%。

## 复现要点

- 复现目标：先跑上游仓库的最小例子，确认核心机制可工作；再跑论文配置，对照原文基线与方法描述。
- 要测量：正确性（往返/精度/输出趋势）、关键配置变化带来的趋势，而非只看单一加速比。
- 不会与原文一致的地方：工艺、器件参数、仿真器版本与基线配置差异都会改变绝对数字；骨架只演示思想。

## 运行证据

- 上游最小例子已实际运行（2026-11-04）：`TetrisG_SDK.py` 瞬间跑完、退出码 0，输入 cnn8-3、group 2，输出 VW-SDK 48、最优 PW 形状 8×4×16×42、16 个窗口、分组 Total CC 32.0。证据见 [runs/tetrisg-20261104/](../../runs/tetrisg-20261104/)。这只证明 TetrisG 脚本能在这里跑通一个配置并输出窗口和周期数，不复现 JETCAS 2026 的论文加速比，也不是芯片实测；NeuroSim 的 C++ 部分没构建、没跑。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
