# 代码说明：CIM-Explorer（CIM-E）：面向 RRAM 交叉阵列的二值/三值神经网络推理优化

- **上游仓库：** https://github.com/rpelke/CIM-E
- **许可证：** Apache
- **硬件/软件需求：** 标准 Linux CPU + Docker（或 Podman，支持 rootless）；仿真构建需 Python 3.10/3.11 与 python3-dev，无需 RRAM 硬件、GPU 或 FPGA

## 完整性清单

- 完整性：Apache 许可证；`src/`（编译器、实验、模型解析、ADC 校准、绘图）、analog-cim-sim 子模块、`models/`、`scripts/`（benchmark.bash、build_simulator.bash、build_tvm.bash）、`docker/`、`util/`；仿真器构建与 Docker 镜像的 CI 检查。
- 上游 HEAD 经 `git ls-remote` 核实：CIM-E 为 f1bb4eac，analog-cim-sim 为 fce1f36e。
- 不能在本机复现的部分：Docker 镜像构建与基准全流程，需要装有 Docker 的机器；裸跑 `main.py` 不是文档路线。

## 最小复现命令

见本篇 README 的“复现要点”一节；命令与预期检查以上游 README 为准。

## 骨架说明

- `reproduce.py` 是原创骨架，仅用 Python 标准库，不是上游代码；它演示核心思想，不复现原文性能数字。
- 复现原文数字需要上游代码、对应硬件/工具链与原文数据/配置；骨架只能验证算法与数据流层面的正确性与相对趋势。

