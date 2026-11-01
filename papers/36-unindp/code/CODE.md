# 代码说明：UniNDP：面向近 DRAM 处理架构的统一编译与仿真工具

- **上游仓库：** https://github.com/UniNDP-hpca25-ae/UniNDP
- **许可证：** MIT
- **硬件/软件需求：** 标准 Linux CPU + Python，无需 UPMEM、GPU 或 FPGA 硬件

## 完整性清单

- 完整性：MIT 许可证；`compile.py`、`compile_detail.py`、`compile_predictor.py`、`frontend/`、`midend/`、`backend/`、`sim/`、`tools/`、`script/`；`workload/` CSV；`config/` 覆盖 upmem、hbm-pim、gddr6-aim、dimmining；测试 `testsim.py`、`sim_verify.py`。
- 上游 HEAD 经 `git ls-remote` 核实为 c8b21684，另有镜像 godfather991/UniNDP。
- 不能仅凭本机复现的部分：完整论文表格（分架构、分工作负载）需按原文与上游工作负载脚本运行；玩具规模输出不是论文数字。

## 最小复现命令

见本篇 README 的“复现要点”一节；命令与预期检查以上游 README 为准。

## 骨架说明

- `reproduce.py` 是原创骨架，仅用 Python 标准库，不是上游代码；它演示核心思想，不复现原文性能数字。
- 复现原文数字需要上游代码、对应硬件/工具链与原文数据/配置；骨架只能验证算法与数据流层面的正确性与相对趋势。

