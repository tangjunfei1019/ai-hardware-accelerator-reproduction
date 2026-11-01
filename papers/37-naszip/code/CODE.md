# 代码说明：NasZip：面向 DIMM 近数据处理的近似最近邻搜索软硬件协同设计

- **上游仓库：** https://github.com/Intelligent-Computing-Research-Group/NasZip
- **许可证：** MuLan PSL 2.0（README 标注；再分发前请核对仓库许可证文件）
- **硬件/软件需求：** 预建索引路线：x86 服务器，16 核以上、256 GB 以上 DRAM；从头构建路线需大显存 GPU，耗时更长

## 完整性清单

- 完整性：README 标注 MuLan PSL 2.0；`simulate/`（cache、detail、FEE、overall、prefetch 仿真器）、`sim_tools/`、`idx_tools/`、`preprocess_idx/`、`Plot/` 绘图脚本、`result/` 预填基线数据；每图 bash 脚本并标注运行时间；论文附录引用 Zenodo 存档 DOI 10.5281/zenodo.19453078。
- 上游 HEAD 经 `git ls-remote` 核实为 a1e96eae。
- 不能在本机复现的部分：全部论文规模仿真与图 8/15/16/19 的完整流水线，需要符合硬件要求的服务器与大数据下载。

## 最小复现命令

见本篇 README 的“复现要点”一节；命令与预期检查以上游 README 为准。

## 骨架说明

- `reproduce.py` 是原创骨架，仅用 Python 标准库，不是上游代码；它演示核心思想，不复现原文性能数字。
- 复现原文数字需要上游代码、对应硬件/工具链与原文数据/配置；骨架只能验证算法与数据流层面的正确性与相对趋势。

