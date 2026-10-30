## 代码来源

- 状态：**仿真工具，无本篇官方芯片代码**。本篇是综述，不附带芯片 RTL。
- 最接近的建模路线（已核实存在）：
  - Timeloop / Accelergy 基础设施：https://github.com/Accelergy-Project/accelergy-timeloop-infrastructure
  - Timeloop / Accelergy 练习：https://github.com/Accelergy-Project/timeloop-accelergy-exercises
- 性质：第三方学术工具（MIT 等机构的建模框架），不是 Sze 综述作者发布的芯片代码；使用前请阅读各仓库自带的许可证。
- 运行思路：先用本目录的 `reproduce.py` 理解数据搬运记账，再用 Timeloop 定义架构与映射，对比不同数据流的访存与能耗。

## 本目录骨架

- `reproduce.py`：原创复现骨架，仅用 Python 标准库，演示三种数据流的访存记账，不是原文代码。
