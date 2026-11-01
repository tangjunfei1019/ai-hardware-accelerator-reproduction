# CIM-Explorer（CIM-E）：面向 RRAM 交叉阵列的二值/三值神经网络推理优化

## 原文信息

- **英文原题：** CIM-Explorer (CIM-E): Optimizing Binary and Ternary Neural Network Inference on RRAM Crossbars
- **作者：** Rebecca Pelke、José Cubero-Cascante、Nils Bosbach 等（亚琛工业大学）
- **发表处：** SAMOS 2025；arXiv:2505.14303
- **上游仓库：** https://github.com/rpelke/CIM-E
- **许可证：** Apache
- **硬件/软件需求：** 标准 Linux CPU + Docker（或 Podman，支持 rootless）；仿真构建需 Python 3.10/3.11 与 python3-dev，无需 RRAM 硬件、GPU 或 FPGA

## 核心方法

- 编译时：用基于 TVM 的编译栈（含 Larq 前端）把二值/三值网络优化到交叉阵列上执行，支持多 batch 与交叉阵列相关优化（如最大化权重重用），支持任意交叉阵列尺寸。
- 运行时：按计算模式准备权重；多个后端可执行，包括不同仿真器。
- 设计空间探索（DSE）工具：自动寻找最优交叉阵列参数与映射，使人在提交芯片设计前就能估计给定交叉阵列的精度。
- 关键区分：多数 RRAM-CIM 工具只覆盖编译、仿真或 DSE 其中一环，且通常假设 8 位量化；本工具把三者打通，并面向二值/三值网络。

## 核心效果

- 贡献是工具与 DSE 流程本身，而非某一个加速器的加速比；分模型、分映射的精度结果以原文为准，本仓库不引用单一 headline 数字。
- 对低精度模拟存算研究者而言，这是本次检索中发现的最完整的开源起点：编译、仿真、DSE 在同一仓库内闭环。
- 注意仓库名：正确链接是 `rpelke/CIM-E`；`rpelke/CIM-Explorer` 经核实不存在，不要使用后者。

## 复现要点

- 最小复现（Docker 路线，按文档）：`git clone --recursive https://github.com/rpelke/CIM-E.git`（含 analog-cim-sim 子模块），`./models/download_models.bash` 下载预编译二值/三值模型，`docker build -f docker/build_simulator.dockerfile -t cim-e .`（或 `docker pull docker.io/pelke/cim-e:latest`），再按 `scripts/benchmark.bash` 与 README “Run Simulations” 一节运行基准。
- 预期检查：Docker 镜像构建成功（仓库有仿真器构建与 Docker 镜像的 CI 检查），基准脚本通过交叉阵列仿真器运行二值/三值推理。
- 诚实说明：本机未端到端运行。`src/main.py --help` 在本机立即失败，报错 `No module named 'tvm'`，因为文档路线是 Docker 而非裸跑 `python src/main.py`；而本虚拟机未安装 Docker。为保持与文档路线一致，未在 Docker 外尝试仿真器构建。在装有 Docker 的机器上，文档的构建-基准流程即为可复现路径。

## 代码来源

- 上游代码见上游仓库链接；本文件夹的 `code/CODE.md` 给出完整性清单与最小复现命令。
- **本文件夹的 `code/reproduce.py` 是原创复现骨架，仅用 Python 标准库，用于理解核心思想，不是上游代码，也不是原文硬件/仿真器，不能直接复现原文数字。**

