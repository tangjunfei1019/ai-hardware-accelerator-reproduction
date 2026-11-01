#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原创复现骨架（仅 Python 标准库），不是上游 Ramulator 代码。

演示 DRAM 控制器统计思想：按踪迹地址逐条访问，统计行命中/
行缺失/行冲突，并估计平均读延迟。行地址用地址高位示意。
"""
# 踪迹：(地址, 是否读)；同一行连续访问为命中，换行同 bank 为冲突
TRACE = [
    (0x1000, True), (0x1040, True), (0x1080, True),
    (0x2000, True), (0x2040, True),
    (0x1000, True), (0x3000, True),
]
ROW_MASK = 0xF000
LATENCY = {"hit": 20, "miss": 45, "conflict": 70}


def simulate(trace):
    open_row = {}
    hits = misses = conflicts = 0
    total_latency = 0
    for addr, _is_read in trace:
        bank = (addr >> 12) & 0x3
        row = addr & ROW_MASK
        if bank not in open_row:
            misses += 1; total_latency += LATENCY["miss"]; open_row[bank] = row
        elif open_row[bank] == row:
            hits += 1; total_latency += LATENCY["hit"]
        else:
            conflicts += 1; total_latency += LATENCY["conflict"]; open_row[bank] = row
    n = len(trace)
    return {"cycles": n, "hits": hits, "misses": misses, "conflicts": conflicts,
            "avg_latency": total_latency / n if n else 0.0}


def main():
    stats = simulate(TRACE)
    print("DRAM 控制器骨架统计：")
    print(f"  访问数 = {stats['cycles']}，行命中 = {stats['hits']}，行缺失 = {stats['misses']}，行冲突 = {stats['conflicts']}")
    print(f"  平均读延迟 = {stats['avg_latency']:.1f} 周期（示意模型，非 Ramulator 输出）")
    assert stats["hits"] + stats["misses"] + stats["conflicts"] == stats["cycles"]
    print("自检通过：命中+缺失+冲突 = 总访问数")


if __name__ == "__main__":
    main()
