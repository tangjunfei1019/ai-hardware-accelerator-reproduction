# UniNDP：面向近 DRAM 处理架构的统一编译与仿真工具

## 原文信息

- **英文原题：** UniNDP: A Unified Compilation and Simulation Tool for Near DRAM Processing Architectures
- **作者：** Tongxin Xie、Zhenhua Zhu、Bing Li 等（清华大学及合作者）
- **发表处：** HPCA 2025（最佳论文荣誉提名）
- **上游仓库：** https://github.com/UniNDP-hpca25-ae/UniNDP
- **许可证：** MIT
- **硬件/软件需求：** 标准 Linux CPU + Python，无需 UPMEM、GPU 或 FPGA 硬件

## 核心方法

- 统一的树形近 DRAM 处理（NDP）硬件抽象与统一指令集：用同一套描述刻画不同 DRAM 技术与处理单元位置，避免每个厂商栈各自为政。
- 周期精确、指令驱动的仿真器：跟踪存储单元与处理单元的状态，为编译器提供性能预测。
- 编译器优化数据切分、映射与工作负载调度，并以硬件状态指导的搜索空间剪枝缩小探索范围。
- 覆盖的架构包括 UPMEM、Samsung HBM-PIM、SK Hynix GDDR6-AiM 与 AxDIMM，工作负载示例包括 ResNet-18、VGG-11、LLaMA-2 7B/13B 的 prefill 与 decode，以及普通矩阵乘法。

## 核心效果

- 论文称，在不同架构与机器学习工作负载上，相对已有映射/编译方法可获得 1.05–3.43 倍加速（不同来源摘要给出的区间略有差异：幻灯片为 1.08–3.37 倍；以原文为准）。
- 更重要的效果是方法论层面的：同一 NDP 思想可在不同架构间比较，而不被锁定在某一家厂商的仿真/编译栈上。
- 本仓库不把工具的玩具规模输出当作论文数字：下文复现要点中的 16×16 矩阵乘法只是编译+仿真流水线能跑通的证据。

## 复现要点

- 最小复现（已在本机实际运行）：`git clone https://github.com/UniNDP-hpca25-ae/UniNDP.git`，`pip install -r requirements.txt`（numpy、PyYAML、tqdm、xlrd、xlsxwriter），`python compile.py -h` 打印完整编译选项，`python compile.py -A upmem -W mm -S 16 16 16 1 -O testout` 在 `test/testout/` 下生成 CSV 与日志。
- 实际运行结果：微型 UPMEM 16×16×16 矩阵乘法写出 `test/testout/csv/_gemm.csv`，日志中 `best_result: 98`、`speedup: 1.0`。对 16×16 的玩具规模，相对自身基线为 1.0 倍并不意外；关键是编译+仿真流水线端到端跑通。
- 诚实说明：工具在本环境最后以非零退出码结束，但此时 CSV 已写出，因此以 CSV/日志为准，而非退出码；完整工作负载（ResNet/LLaMA 的 CSV）未运行，那是更长、论文规模的运行。

## 代码来源

- 上游代码见上游仓库链接；本文件夹的 `code/CODE.md` 给出完整性清单与最小复现命令。
- **本文件夹的 `code/reproduce.py` 是原创复现骨架，仅用 Python 标准库，用于理解核心思想，不是上游代码，也不是原文硬件/仿真器，不能直接复现原文数字。**

