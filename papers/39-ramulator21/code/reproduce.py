#!/usr/bin/env python3
"""Original reproduction skeleton (Python standard library only), not upstream Ramulator code.

Demonstrates DRAM controller statistics: walk an address trace, count
row hits / row misses / row conflicts, and estimate average read latency.
Row address is illustrated with the high bits of the address.
"""
# Trace: (address, is_read); consecutive accesses to the same row are hits, a row change in the same bank is a conflict
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
    print("DRAM controller skeleton statistics:")
    print(f"  Accesses = {stats['cycles']}, row hits = {stats['hits']}, row misses = {stats['misses']}, row conflicts = {stats['conflicts']}")
    print(f"  Average read latency = {stats['avg_latency']:.1f} cycles (illustrative model, not a Ramulator output)")
    assert stats["hits"] + stats["misses"] + stats["conflicts"] == stats["cycles"]
    print("Self-check passed: hits + misses + conflicts = total accesses")


if __name__ == "__main__":
    main()
