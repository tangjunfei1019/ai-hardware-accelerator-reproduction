#!/usr/bin/env python3
"""Original reproduction skeleton (Python standard library only), not upstream UniNDP code.

Demonstrates the unified NDP compile/simulate idea: tile a matrix
multiplication across a DRAM hierarchy, map it to processing units,
and estimate cycles with a simple cost model.
"""
import math

# Architecture abstraction: parallel processing units and MACs per PU per cycle (illustrative)
ARCHS = {
    "upmem": {"pus": 16, "mac_per_pu": 1},
    "hbm-pim": {"pus": 32, "mac_per_pu": 2},
    "gddr6-aim": {"pus": 16, "mac_per_pu": 2},
}


def compile_and_simulate(m, n, k, arch):
    """Tiling + mapping + cycle estimate: total MACs over parallel MAC capacity, plus data-movement overhead."""
    cfg = ARCHS[arch]
    total_macs = m * n * k
    parallel = cfg["pus"] * cfg["mac_per_pu"]
    compute_cycles = math.ceil(total_macs / parallel)
    # Movement overhead: weights and inputs amortised over ranks (illustrative model, not the original simulator)
    move_cycles = math.ceil((m * k + k * n) / cfg["pus"])
    return compute_cycles + move_cycles


def main():
    m = n = k = 16
    print("Unified NDP skeleton: 16x16x16 matmul, estimated cycles per architecture")
    for arch in ARCHS:
        print(f"  {arch}: estimated cycles = {compile_and_simulate(m, n, k, arch)}")
    # Self-check: the more parallel architecture should not estimate more cycles
    assert compile_and_simulate(m, n, k, "hbm-pim") <= compile_and_simulate(m, n, k, "upmem")
    print("Self-check passed: one compile/simulate flow can compare different architectures")


if __name__ == "__main__":
    main()
