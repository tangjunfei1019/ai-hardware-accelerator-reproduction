"""Reproduction skeleton (original, not the paper's code): PIM-style
partitioned vector addition.

Standard library only. Demonstrates: splitting a vector by the number of
DPUs, computing one slice per DPU, and merging at the end, matching direct
addition, and printing the DPU count and time (skeleton time, not the
paper's DPU kernel time).
Run: python3 reproduce.py
"""

import time


def main():
    n = 1_000_000
    a = list(range(n))
    b = list(range(n))
    for nr_dpus in (1, 4, 16):
        chunk = n // nr_dpus
        start = time.perf_counter()
        parts = []
        for d in range(nr_dpus):
            lo, hi = d * chunk, (d + 1) * chunk if d < nr_dpus - 1 else n
            parts.extend(a[i] + b[i] for i in range(lo, hi))
        elapsed = time.perf_counter() - start
        print(f"DPU count: {nr_dpus}, result correct: "
              f"{parts == [2 * i for i in range(n)]}, "
              f"time (s): {elapsed:.4f}")
    print("Key point: PrIM's core idea is to compute on the DPU beside the "
          "bank, keeping data there, instead of moving data back to the "
          "host; how you partition directly decides scalability.")


if __name__ == "__main__":
    main()
