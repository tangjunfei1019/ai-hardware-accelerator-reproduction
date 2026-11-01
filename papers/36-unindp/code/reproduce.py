#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原创复现骨架（仅 Python 标准库），不是上游 UniNDP 代码。

演示统一 NDP 编译/仿真思想：把一个矩阵乘法按不同架构的
DRAM 层级切分、映射到处理单元，并用简单代价模型估计周期数。
"""
import math

# 架构抽象：每架构的并行处理单元数与每单元每周期 MAC 数（示意值）
ARCHS = {
    "upmem": {"pus": 16, "mac_per_pu": 1},
    "hbm-pim": {"pus": 32, "mac_per_pu": 2},
    "gddr6-aim": {"pus": 16, "mac_per_pu": 2},
}


def compile_and_simulate(m, n, k, arch):
    """切分 + 映射 + 周期估计：总 MAC 数除以并行 MAC 能力，再加数据搬运开销。"""
    cfg = ARCHS[arch]
    total_macs = m * n * k
    parallel = cfg["pus"] * cfg["mac_per_pu"]
    compute_cycles = math.ceil(total_macs / parallel)
    # 搬运开销：权重与输入按 rank 数分摊（示意模型，非原文仿真器）
    move_cycles = math.ceil((m * k + k * n) / cfg["pus"])
    return compute_cycles + move_cycles


def main():
    m = n = k = 16
    print("统一 NDP 骨架：矩阵乘法 16x16x16，分架构周期估计")
    for arch in ARCHS:
        print(f"  {arch}: 估计周期 = {compile_and_simulate(m, n, k, arch)}")
    # 自检：并行度更高的架构估计周期不应更大
    assert compile_and_simulate(m, n, k, "hbm-pim") <= compile_and_simulate(m, n, k, "upmem")
    print("自检通过：统一抽象下不同架构可用同一编译/仿真流程比较")


if __name__ == "__main__":
    main()
