# Eyeriss：面向深度卷积神经网络的节能可重构加速器

## 原文信息

- 原文标题：Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks
- 作者：Yu-Hsin Chen、Tushar Krishna、Joel Emer、Vivienne Sze
- 年份与发表处：2017，IEEE Journal of Solid-State Circuits（ISSCC 特刊）

## 核心方法

- 空间架构：168 个 PE 排成阵列，每个 PE 有自己的寄存器文件、乘加单元和控制；全局缓冲（GLB）居中分发，片外 DRAM 在最外层，形成四级存储层次。
- 行固定（Row-Stationary, RS）数据流：把一维卷积的行留在 PE 寄存器文件里复用，权重、激活、部分和在阵列内以组播方式流动，最大化三类数据的复用，减少 DRAM 与 GLB 访问。
- 可重构组播片上网络（NoC）：根据不同卷积层的形状（滤波器尺寸、通道数）重新配置数据分发方式，避免固定数据流在某些层上利用率低。
- 稀疏与门控：对零激活做数据门控与压缩，进一步省功耗、省带宽；芯片与 Caffe 框架打通，可直接跑真实网络。

## 核心效果

- 论文报告的芯片实测要点（以原文为准）：168 PE 阵列，65 nm 工艺；在 AlexNet 卷积层上约 35 fps、约 278 mW，作者报告比同期移动 GPU 能效高约 10 倍量级。
- RS 数据流相对其他数据流的能效优势在 1.4 倍至 2.5 倍量级（随层形状变化），这是理解“数据流即架构”的关键数字。
- Eyeriss v2（2019，后续工作）进一步面向紧凑与稀疏网络，引入分层网格 NoC 与 RS+ 数据流，但本篇总结以 2017 年 Eyeriss 为准。

## 复现要点

- 复现目标：对一个卷积层，分别实现权重固定、输出固定、行固定三种数据流的访存记账，验证行固定在多数层上的优势与个别层上的劣势。
- 要测量：DRAM/GLB/RF 访问量、PE 利用率、不同滤波器尺寸与通道数下的数据流排名变化。
- 不会与原文芯片一致的地方：真实 NoC 拥塞、时钟、65 nm 功耗与面积；骨架只做数据流层面的相对比较。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码，也不是芯片 RTL。它只用于理解核心思想，不能直接复现原文的面积、功耗与时钟数字。
