# ColumnQuant / RUnQuant：面向存内计算加速器的列粒度量化

## 原文信息

- 仓库对应论文：Column-wise Quantization of Weights and Partial Sums for Accurate and Efficient Compute-In-Memory Accelerators，DATE 2025，arXiv:2502.07842，作者 Jiyoon Kim 等
- 同一仓库的后续论文（据 SKKU IRIS Lab 页面）：RUnQuant: High-Resolution Weight Quantization via Unanchored Weight Decomposition in Column-wise Granularity for CIM Accelerators，Journal of Systems Architecture，2026（2026-01-17 发布）
- 中文标题：ColumnQuant / RUnQuant：面向存内计算加速器的列粒度量化
- 上游仓库：https://github.com/jiyoonkm/ColumnQuant

## 核心方法

- 列粒度对齐：权重与部分和用同一列粒度的一致缩放因子量化，而不是层粒度/通道粒度不匹配，从而使阵列内的 MAC 结果与反量化保持一致。
- 无锚权重分解（RUnQuant）：不采用传统的零锚分解，而是在不固定零锚的情况下分解权重，从而在低精度单元下增加可表示的量化等级，并去掉两阶段训练过程。
- 框架：`SplitConv4Pim_group.py` 实现面向 CIM 的卷积（按每单元比特数拆分权重、权重量化与部分和量化的 LSQ、分组卷积、按行切分的部分和量化），含三种层变体（普通、权重分解、权重分解 + 面向二值 RRAM 的改进 LSQ）。

## 核心效果

- 据 RUnQuant 的 SKKU 页面：相对现有方法精度提升最高 4.05%，同时保持反量化开销。据更早列粒度论文的综述摘要：在不同模型上相对最佳可比方法提升约 0.99%、2.69% 与 1.01%（实验为 CIFAR-10/100 与 ImageNet 上的 ResNet-20/18）。各模型的具体表格以原文为准；这里的数字引自上述二次摘要，本次未重新测量。
- 影响：它直面模拟存内计算实践中占主导的两项成本——ADC 开销与交叉阵列单元精度受限，并给出可实际运行的卷积框架，而不只是描述思想。

## 复现要点

- 复现目标：按列计算缩放因子并做 3-bit 量化与反量化，比较列粒度量化与层粒度量化的误差。
- 要测量：不同粒度下的量化误差；不要把骨架输出当作原文精度提升。
- 不会与原文工具一致的地方：完整的 PyTorch 训练流程、LSQ 学习过程、ResNet 训练精度；骨架只演示列粒度量化的思想。

## 代码来源

见 [`code/CODE.md`](code/CODE.md)，以及本目录的复现骨架 [`code/reproduce.py`](code/reproduce.py)。

> 注意：本目录的 `reproduce.py` 是原创复现骨架，不是原文作者的代码。它只用于理解核心思想，不能直接复现原文的精度数字。

## 本次核实说明

- 上游仓库经 `git ls-remote` 核实存在；框架文件 `SplitConv4Pim_group.py`、`LSQ.py`、`any_quant.py` 通过 `python3 -m py_compile` 语法检查。
- 完整克隆列表中还包括 `main.py`、`resnet_quan.py`、`utils.py`（仅按文件名列出，内容本次未逐项检查，端到端复现时请先检查）与 `legacy/` 目录中的 ResNet-20 CIFAR-100 W3A3P3 检查点（`ResNet20_Cifar100_W3A3P3_ckpt.pth`）。
- 本次未端到端运行上游，原因是该虚拟机没有安装 PyTorch，且 CPU 版 PyTorch 下载多次超时——这是环境限制，不是仓库缺陷。
- 最弱的完整性点：仓库根目录未找到许可证文件与 requirements 文件；再分发或做产品前请先与作者/论文许可条款核对。
