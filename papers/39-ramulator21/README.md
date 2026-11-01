# Ramulator 2.1：面向现代 DRAM 系统的可组合存储系统仿真器

## 原文信息

- **英文原题：** Ramulator 2.1: A Composable Memory System Simulator for Modern DRAM Systems
- **作者：** Haocong Luo、F. Nisa Bostancı、Ataberk Olgun 等（SAFARI 研究组，苏黎世联邦理工学院及合作者）
- **发表处：** 2026（Ramulator 与 DRAM Bender 教程，与 ICS 同期）；arXiv:2606.13844
- **上游仓库：** https://github.com/CMU-SAFARI/ramulator2
- **许可证：** MIT
- **硬件/软件需求：** 标准 Linux CPU + C++ 工具链（cmake、GCC）+ Python 3.10+，无需 GPU、FPGA 或 DRAM 硬件

## 核心方法

- **范围说明：本篇不是存算一体加速器论文，而是 DRAM/存储系统仿真器。** 它是存算一体与近数据处理研究评估一切触及 DRAM 的设计时所依赖的基础设施，因此列入本组；切勿把它表述为一种 CIM 架构。
- 清晰模块化的 C++ 代码库与自动生成的 Python 包装：用户用 Python 写高层 DRAM 规约，框架自动生成 Python 代理，隐藏底层 C++ 样板代码。
- 周期级 DRAM 器件与存储控制器模型：可独立在存储踪迹上运行，也可作为库嵌入其他仿真器（提供 gem5 包装，支持 SE 与 FS 模式）。
- 两层验证：细粒度时序约束/调度检查，以及系统级延迟-吞吐曲线；另有 DRAM 命令踪迹可视化工具。
- 覆盖的现代标准包括 DDR3/4/5、GDDR6/7、LPDDR5/6、HBM1–4，以及对存算一体研究关键的 DDR4_PUM（processing-using-DRAM）。

## 核心效果

- 价值不以 TOPS/W 衡量，而以覆盖范围、易用性与验证质量衡量：这是仿真器，而非加速器，因此本仓库不引用任何加速比。
- SAFARI 研究组的 Ramulator 系列是存储系统文献中的标准 DRAM 仿真器；2026 年这次大改版加入 HBM4、LPDDR6、GDDR7 与 DDR4_PUM 支持，是整个存算一体领域后续工作都会用到的评估基础。
- 论文/教程中的验证结果以原文为准；本机运行的只是示例踪迹自身的统计量，不是论文结果。

## 复现要点

- 最小复现（已在本机实际运行）：`git clone https://github.com/CMU-SAFARI/ramulator2.git`，`bash build.sh`（cmake 配置+构建；本机配置约 44 秒，完整构建数分钟），`PYTHONPATH=$PWD/python python3 examples/example_config.py`。
- 实际运行结果：配置完成（cmake、GCC 13.3、Python 3.12.3，生成 14 种 DRAM 标准、52 个 Python 组件包装），构建完成，示例运行输出：控制器周期 81302，平均读延迟 45.2 周期，读请求 6、写请求 0、行命中 3、行缺失 3、行冲突 0。
- 诚实说明：以上是示例踪迹自身的统计量，不是论文结果；完整测试套件（`tests/`）未运行，那是更长的验证路线。

## 代码来源

- 上游代码见上游仓库链接；本文件夹的 `code/CODE.md` 给出完整性清单与最小复现命令。
- **本文件夹的 `code/reproduce.py` 是原创复现骨架，仅用 Python 标准库，用于理解核心思想，不是上游代码，也不是原文硬件/仿真器，不能直接复现原文数字。**

