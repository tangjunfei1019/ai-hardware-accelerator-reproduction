# 代码来源与复现说明：NVDLA

- 链接：https://github.com/nvdla/hw
- 性质：官方开源 RTL，非第三方实现。
- 许可证：NVIDIA Open NVDLA License and Agreement v1.0（`LICENSE`，商业使用前请先读；它不是普通的 MIT/BSD 许可证）。

## 完整性清单

- [x] 真实代码，不只是 PDF：Verilog RTL（`vmod/nvdla`、`vmod/vlibs`、`vmod/rams`，`vmod/` 下 406 个 `.v` 文件）、SystemC C 模型（`cmod/`）、trace 播放测试台（`verif/`，含示例 trace）、综合脚本（`syn/`）、性能估计（`perf/`）
- [x] 安装/运行说明：README（基本构建 + 健全性仿真）与 nvdla.org 上的集成手册
- [x] 示例：`verif/traces/` 中各网络的示例 trace；`tools/bin/` 含 `tmake`、`run_sanity`、`vcp`、`defgen`
- [x] 硬件需求：标准 Linux 机器即可做 RTL 仿真/综合；FPGA/ASIC 流程可选，用于实现；仿真 RTL 不需要 NVIDIA GPU

## 最小复现步骤（上游，文档路径）

```bash
git clone https://github.com/nvdla/hw
cd hw
bin/tmake
```

预期检查（据仓库 README）：`tmake` 编译设计并运行一次简短的健全性仿真。完整集成需要集成手册（nvdla.org/integration_guide.html）与 Verilog 仿真/综合工具链。

## 不能仅凭本文复现的部分

- 真实 RTL 的面积、功耗、时钟与 trace 播放性能，需要 Verilog 工具链与所选配置；骨架只演示流水线阶段。
- 本次未端到端运行上游，原因是该虚拟机未安装完整的 Verilog 仿真/综合工具链。

## 本目录骨架

`reproduce.py` 为原创标准库骨架，演示卷积 → 激活 → 池化的流水线，与上游代码无关。
