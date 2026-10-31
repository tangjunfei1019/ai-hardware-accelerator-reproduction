"""复现骨架（原创，非原文代码）：PIM 式分区向量加法。

只用 Python 标准库。演示：把向量按 DPU 数量切分，
每核算一段，最后汇总，与直接相加结果一致，
并打印分区数与耗时（骨架耗时，非原文 DPU 核时间）。
运行：python3 reproduce.py
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
        print(f"DPU 数: {nr_dpus}，结果正确: {parts == [2 * i for i in range(n)]}，"
              f"耗时（秒）: {elapsed:.4f}")
    print("要点：PrIM 的核心思想是把数据留在 bank 旁的 DPU 上算，"
          "而不是把数据搬回主机；分区方式直接决定扩展性。")


if __name__ == "__main__":
    main()
