# 代码来源与复现说明：TetrisG-SDK：面向快速存内计算的自适应窗口与分组卷积映射框架

## 可复现等级：A

- A = 上游代码可在标准机器 / 仿真器上运行。
- B = 上游代码可运行，但需要特殊硬件或特定工具链。
- 本篇等级：**A**。

## 上游仓库（已核实存在）

- 链接：https://github.com/SybilD/TetrisG-SDK
- 仓库内容：TetrisG_SDK.py、Tetris_SDK.py、.ipynb 演示、NeuroSim 目录、demo 视频与流程图（注意仓库根文件名为 readme.md）
- 硬件 / 软件要求：标准 CPU，Python；仓库含 .py/.ipynb 与 NeuroSim 目录，按仓库 readme.md 的依赖安装
- 许可证：以该仓库自带许可证文件为准；使用前请先阅读。

## 复现步骤

1) git clone https://github.com/SybilD/TetrisG-SDK
2) 按 readme.md 安装依赖
3) 先跑 TetrisG_SDK.py 或 .ipynb 小例子，确认窗口搜索与分组逻辑
4) 再跑 CNN8 等模型配置，对照原文表
预期检查：小例子应输出窗口配置与利用率；模型配置应输出延迟/能量估计趋势。

## 不能仅凭论文复现的部分

- 不能把骨架的利用率数字当作 NeuroSim 仿真结果；不能忽略分组卷积对精度的约束，原文称近无损，需以原文实验为准。

## 本目录骨架说明

- `reproduce.py` 是原创 Python 标准库骨架，演示核心思想，不是上游代码，也不是 RTL/芯片实测。
- 骨架本身不满足本篇的可复现要求；可复现性由上面上游仓库的步骤保证。
