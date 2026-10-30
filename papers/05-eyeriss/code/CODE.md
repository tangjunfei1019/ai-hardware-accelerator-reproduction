## 代码来源

- 状态：**第三方 RTL，已核实存在，但不是 MIT 官方发布**。请勿将其标注为原作者官方代码。
- 已核实存在的第三方仓库（通过 GitHub 内容读取核实）：
  - https://github.com/abdelrahmanmedhatt/Eyeriss （含 GLB/HMNOC/PE 的 Verilog 文件）
  - https://github.com/arasi15/CNN-Accelerator-Implementation-based-on-Eyerissv2 （含 RTL 目录与 README）
- 使用前请阅读各仓库自带的许可证与 README；第三方实现与原文芯片在功能、时序与精度上可能有差异，复现结论要以你自己的测试为准。
- 建模路线补充：Timeloop/Accelergy（见 Sze 一节链接）可用于数据流层面的建模与比较。

## 本目录骨架

- `reproduce.py`：原创复现骨架，仅用 Python 标准库，演示行固定数据流的行级复用记账，不是原文代码，也不是上述第三方代码的拷贝。
