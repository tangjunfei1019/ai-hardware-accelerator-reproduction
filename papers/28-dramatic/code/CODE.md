# 代码来源与复现说明：DRAMatic：面向同态加密运算的 UPMEM 存内处理加速

## 可复现等级：B

- A = 上游代码可在标准机器 / 仿真器上运行。
- B = 上游代码可运行，但需要特殊硬件或特定工具链。
- 本篇等级：**B**。

## 上游仓库（已核实存在）

- 链接：https://github.com/UzL-ITS/DRAMatic-Speedup
- 仓库内容：C++ UPMEM DPU 代码、同态加密基础运算（BGV 乘法、NTT/iNTT、模加/模乘）、RNS 优化实现
- 硬件 / 软件要求：完整速度复现需要 UPMEM PIM 硬件（DPU DIMM）与 UPMEM SDK；无硬件时只能编译与读代码，不能复现论文的硬件加速比
- 许可证：以该仓库自带许可证文件为准；使用前请先阅读。

## 复现步骤

1) git clone https://github.com/UzL-ITS/DRAMatic-Speedup
2) 按仓库说明安装 UPMEM SDK，确认 DPU 工具链可用
3) 在有 UPMEM 硬件的机器上编译并跑最小 NTT/模乘例子
4) 再跑 BGV 乘法案例，对照原文参数与基线
预期检查：最小例子应在 DPU 上正确完成 NTT/iNTT 往返；无硬件时应明确记录为未复现硬件部分。

## 不能仅凭论文复现的部分

- 不能在普通 CPU 上复现 334 倍这一硬件加速比；不能把 CPU 模拟结果当作 DPU 实测；功耗数字需有 UPMEM 硬件测量条件才可比。

## 本目录骨架说明

- `reproduce.py` 是原创 Python 标准库骨架，演示核心思想，不是上游代码，也不是 RTL/芯片实测。
- 骨架本身不满足本篇的可复现要求；可复现性由上面上游仓库的步骤保证。
