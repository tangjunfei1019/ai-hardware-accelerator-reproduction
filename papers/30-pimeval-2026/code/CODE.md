# 代码来源与复现说明：PIMeval-PIMbench 2026 扩展：面向数字 DRAM PIM 的建模与基准扩展

## 可复现等级：A

- A = 上游代码可在标准机器 / 仿真器上运行。
- B = 上游代码可运行，但需要特殊硬件或特定工具链。
- 本篇等级：**A**。

## 上游仓库（已核实存在）

- 链接：https://github.com/UVA-LavaLab/PIMeval-PIMbench
- 仓库内容：C++ PIMeval 仿真器、PIMbench 基准套件、子阵列级位串行/位并行与 bank 级位并行三种数字 PIM 模型、roofline 分析工具
- 硬件 / 软件要求：标准 Linux 机器，C++ 工具链；不需要 UPMEM 硬件即可跑仿真器与基准（真实硬件对比需另行说明）
- 许可证：以该仓库自带许可证文件为准；使用前请先阅读。

## 复现步骤

1) git clone https://github.com/UVA-LavaLab/PIMeval-PIMbench
2) 按仓库 wiki / README 编译仿真器与基准
3) 先跑最小基准，确认三种 PIM 模型可切换
4) 再跑 roofline 分析，对照原文方法
预期检查：最小基准应输出延迟与能量估计；roofline 应随运算强度呈现 PIM 与 CPU/GPU 的交叉趋势。

## 不能仅凭论文复现的部分

- 不能把仿真器估计直接等同于真实 DRAM PIM 芯片实测；不能忽略 DRAM 技术参数（DDR/HBM、GDL 宽度）对结论的影响。

## 本目录骨架说明

- `reproduce.py` 是原创 Python 标准库骨架，演示核心思想，不是上游代码，也不是 RTL/芯片实测。
- 骨架本身不满足本篇的可复现要求；可复现性由上面上游仓库的步骤保证。
