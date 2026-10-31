# 代码来源与复现说明：Gemmini

- 链接：https://github.com/ucb-bar/gemmini
- 性质：官方开源生成器，Chisel RTL。
- 许可证：UC Regents 许可证（`LICENSE`，再分发有条件，使用前请先读该文件）。

## 完整性清单

- [x] 真实代码，不只是 PDF：Chisel RTL 生成器（`src/`，61 个 Scala 文件）、软件栈（`software/libgemmini`、`software/gemmini-rocc-tests`）、建模（`modeling/`）
- [x] 安装/运行说明：README“Quick Start”（Chipyard + Spike 配置、软件构建、Verilator 模拟器构建）
- [x] 示例：`software/gemmini-rocc-tests`（从矩阵乘法测试到 ResNet-50 级程序）、JSON 测试配置（`gemmini-tests.json`、`gemmini-smoke.json`）
- [x] 测试：`src/test/` Scala 测试
- [x] 硬件需求：标准 Linux 机器即可做生成器与 Spike/Verilator 仿真；FPGA（FireSim）可选，用于快速周期精确仿真；不需要定制硅片即可运行生成器

## 最小复现步骤（上游，文档路径）

```bash
git clone https://github.com/ucb-bar/chipyard.git
cd chipyard
./build-setup.sh
source env.sh
cd generators/gemmini
make -C software/libgemmini install
cd chipyard/generators/gemmini/software/gemmini-rocc-tests
./build.sh
# 在 chipyard/sims/verilator 下构建周期精确模拟器：
make CONFIG=GemminiRocketConfig
```

预期检查：`build/` 下出现 RISC-V 二进制（裸机、Linux 与代理内核版本），且 `GemminiRocketConfig` 的 Verilator 模拟器构建成功。这是重型构建（Chipyard + RISC-V 工具链 + Verilator），首次运行请按小时计，不是按分钟计。

## 不能仅凭本文复现的部分

- 真实 RTL 综合面积、功耗、时钟频率与 FireSim 周期精确性能，需要完整工具链与所选配置；骨架只演示分块矩阵乘。
- 本次未端到端构建上游，原因是多小时工具链构建未尝试。

## 本目录骨架

`reproduce.py` 为原创标准库骨架，演示分块矩阵乘与输出平稳的思想，与上游代码无关。
