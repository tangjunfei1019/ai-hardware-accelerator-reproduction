## 代码来源

- 状态：**仿真工具，谷歌 TPU 硬件本身不开源**。不要把任何第三方 TPU 复刻标注为谷歌官方代码。
- 已核实存在的建模工具：
  - SCALE-Sim：https://github.com/scalesim-project/SCALE-Sim （脉动阵列加速器仿真器，Python）
  - Timeloop/Accelergy：https://github.com/Accelergy-Project/accelergy-timeloop-infrastructure
- 使用前请阅读各仓库自带的许可证；SCALE-Sim 的新旧版本（ARM-software 版已归档，scalesim-project 版在维护）请以仓库 README 为准。
- 本目录只有原创复现骨架，不含任何上游代码拷贝。

## 本目录骨架

- `reproduce.py`：原创复现骨架，仅用 Python 标准库，演示小型脉动阵列式矩阵乘法，不是原文代码。
