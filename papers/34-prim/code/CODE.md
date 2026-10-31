# 代码来源与复现说明：PrIM

- 链接：https://github.com/CMU-SAFARI/prim-benchmarks
- 性质：官方开源基准集，非第三方实现。
- 许可证：MIT（`LICENSE`，SAFARI Research Group，ETH Zürich，2021）。

## 完整性清单

- [x] 真实代码，不只是 PDF：16 个基准目录（BFS、BS、GEMV、HST-L、HST-S、MLP、NW、RED、SCAN-RSS、SCAN-SSA、SEL、SpMV、TRNS、TS、UNI、VA）+ `Microbenchmarks/`，每个基准含主机 + DPU + 支撑代码
- [x] 安装/运行说明：README（引用、基准列表）+ 各基准的 Makefile 与 README
- [x] 示例：每个基准本身就是可运行示例；`run_*.py` 脚本跑扩展性研究
- [x] 测试/基线：各基准的 `baselines/cpu` 与 `baselines/gpu`
- [ ] 完整结果的硬件需求：UPMEM PIM DIMM + UPMEM SDK（DPU Makefile 需要 `dpu-pkg-config`、`dpu-upmem-dpurte-clang`）。CPU 基线只需要 GCC + OpenMP。

## 最小复现步骤（上游，CPU 基线，已实际运行）

```bash
git clone https://github.com/CMU-SAFARI/prim-benchmarks
cd prim-benchmarks/VA/baselines/cpu
make
./va -t 8 -w 1 -e 3 -i 16777216
```

本次实际输出（标准 CPU，无 UPMEM）：

```
nr_elements	16777216	Kernel Time (ms): 59.957000
```

这是向量加法（VA）基准的 CPU 基线，不是 DPU 结果。

## 完整 DPU 复现（需要 UPMEM 硬件）

```bash
# 例如在 VA/ 目录下，已安装 UPMEM SDK 时：
make NR_DPUS=1 NR_TASKLETS=16 BL=10 TYPE=INT32
./bin/host_code
```

预期检查：主机代码加载 DPU 二进制，在 DPU 上运行负载并报告核时间。本次未运行——该虚拟机没有 UPMEM 硬件与 SDK。

## 本目录骨架

`reproduce.py` 为原创标准库骨架，演示把向量按 DPU 数量分区计算，与上游代码无关。
