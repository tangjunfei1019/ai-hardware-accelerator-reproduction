## 代码来源

- 状态：**仿真工具，原论文的周期级仿真器未发布**。不要把任何第三方 SCNN 复刻标注为原作者官方代码。
- 已核实存在的建模工具：
  - Sparseloop MICRO22 制品：https://github.com/Accelergy-Project/micro22-sparseloop-artifact （Sparseloop 可建模包括 SCNN 在内的稀疏张量加速器）
- 使用前请阅读该仓库自带的许可证与 README；Sparseloop 是分析建模工具，不是 SCNN 的原始周期级仿真器，结论口径不同。
- 本目录只有原创复现骨架，不含任何上游代码拷贝。

## 本目录骨架

- `reproduce.py`：原创复现骨架，仅用 Python 标准库，演示压缩稀疏卷积与散射累加，不是原文代码。
