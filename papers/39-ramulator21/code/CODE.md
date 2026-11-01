# 代码说明：Ramulator 2.1：面向现代 DRAM 系统的可组合存储系统仿真器

- **上游仓库：** https://github.com/CMU-SAFARI/ramulator2
- **许可证：** MIT
- **硬件/软件需求：** 标准 Linux CPU + C++ 工具链（cmake、GCC）+ Python 3.10+，无需 GPU、FPGA 或 DRAM 硬件

## 完整性清单

- 完整性：MIT 许可证；C++ `src/`（DRAM、控制器、前端、存储系统、功耗、地址转换）、`python/`（自动生成包装）、`tests/`（单元、控制器调度、器件时序、延迟-吞吐、功耗、冒烟）、`examples/`、可视化工具；gem5 集成。
- 上游 HEAD 经 `git ls-remote` 核实为 1bb52cee。
- 不能仅凭本机复现的部分：完整测试套件与 gem5 集成验证，需更长运行时间与 gem5 环境。

## 最小复现命令

见本篇 README 的“复现要点”一节；命令与预期检查以上游 README 为准。

## 骨架说明

- `reproduce.py` 是原创骨架，仅用 Python 标准库，不是上游代码；它演示核心思想，不复现原文性能数字。
- 复现原文数字需要上游代码、对应硬件/工具链与原文数据/配置；骨架只能验证算法与数据流层面的正确性与相对趋势。

