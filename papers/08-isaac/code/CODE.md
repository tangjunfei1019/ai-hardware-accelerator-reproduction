## 代码来源

- 状态：**仿真工具，无官方 ISAAC 代码**。ISAAC 原始实现在本次核查中没有确认的公开仓库。
- 已核实存在的建模工具：
  - DNN NeuroSim V1.4（推理侧）：https://github.com/neurosim/DNN_NeuroSim_V1.4
  - DNN NeuroSim V2.1（片上训练侧）：https://github.com/neurosim/DNN_NeuroSim_V2.1
- 性质：学术界广泛使用的存算一体基准框架，不是 ISAAC 作者发布的原始代码；使用前请阅读各仓库自带的许可证，并注意版本（V1.x 与 V2.x 的侧重点不同）。
- 本目录只有原创复现骨架，不含任何上游代码拷贝。

## 本目录骨架

- `reproduce.py`：原创复现骨架，仅用 Python 标准库，演示交叉阵列 MVM 与位切片，不是原文代码。
