# 代码来源与复现说明：CIM-Tuner：通过硬件-映射协同探索平衡 SRAM-CIM 计算与存储容量

## 可复现等级：A

- A = 上游代码可在标准机器 / 仿真器上运行。
- B = 上游代码可运行，但需要特殊硬件或特定工具链。
- 本篇等级：**A**。

## 上游仓库（已核实存在）

- 链接：https://github.com/champloo2878/CIM-Tuner
- 仓库内容：Python 工具、cim_config/、nn_config/、experiments/、evacim/、Result/、requirements.txt（注意仓库根文件名为 Readme.md）
- 硬件 / 软件要求：标准 CPU，Python，见上游 requirements.txt
- 许可证：以该仓库自带许可证文件为准；使用前请先阅读。

## 复现步骤

1) git clone https://github.com/champloo2878/CIM-Tuner
2) pip install -r requirements.txt
3) 按仓库 Readme.md 跑 experiments/ 下的示例配置
4) 改面积预算或宏配置，观察能效/吞吐 Pareto 变化
预期检查：示例应输出配置与能效/吞吐估计；面积约束收紧时，可行配置集应缩小。

## 不能仅凭论文复现的部分

- 不能直接复现原文的硅验证精度；不能把工具的估计值当作流片实测值；面积与工艺假设以原文与仓库配置为准。

## 本目录骨架说明

- `reproduce.py` 是原创 Python 标准库骨架，演示核心思想，不是上游代码，也不是 RTL/芯片实测。
- 骨架本身不满足本篇的可复现要求；可复现性由上面上游仓库的步骤保证。
