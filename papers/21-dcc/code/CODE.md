# 代码来源与复现说明：DCC：面向存内处理架构的数据中心机器学习内核编译器

## 可复现等级：B

- A = 上游代码可在标准机器 / 仿真器上运行。
- B = 上游代码可运行，但需要特殊硬件或特定工具链。
- 本篇等级：**B**。

## 上游仓库（已核实存在）

- 链接：https://github.com/SPIN-Research-Group/DCC
- 仓库内容：C++ 编译器源码、setup.sh、run_experiments.sh、src/，面向 UPMEM/HBM-PIM/AttAcc 等多后端的数据布局与调度
- 硬件 / 软件要求：标准 CPU 可跑编译器前端；完整复现论文数字需要 AttAcc / HBM-PIM 后端仿真器，见上游 setup.sh 与 README
- 许可证：以该仓库自带许可证文件为准；使用前请先阅读。

## 复现步骤

1) git clone https://github.com/SPIN-Research-Group/DCC
2) 按仓库 README / setup.sh 安装依赖并阅读后端说明
3) 先跑仓库自带小例子，确认编译器能生成目标后端代码
4) 再按 run_experiments.sh 跑论文实验脚本，对照论文表中的基线
预期检查：小例子应正常生成代码并输出性能预测；完整后端数字只有在对应 PIM 后端仿真环境下才可比。

## 不能仅凭论文复现的部分

- 不能仅用普通 CPU 复现 HBM-PIM/AttAcc 的绝对加速比；不能把编译器在 CPU 上的运行时间当作 PIM 执行时间；上游仓库的许可证以仓库自带文件为准。

## 本目录骨架说明

- `reproduce.py` 是原创 Python 标准库骨架，演示核心思想，不是上游代码，也不是 RTL/芯片实测。
- 骨架本身不满足本篇的可复现要求；可复现性由上面上游仓库的步骤保证。
