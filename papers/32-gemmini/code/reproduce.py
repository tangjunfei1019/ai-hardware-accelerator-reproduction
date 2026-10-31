"""复现骨架（原创，非原文代码）：脉动阵列式分块矩阵乘。

只用 Python 标准库。演示：把矩阵乘法按 2x2 分块切分，
每块先算局部乘积再累加，得到与直接矩阵乘相同的结果，
同时统计有效乘法次数。
运行：python3 reproduce.py
"""

import random


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def tiled_matmul(a, b, tile=2):
    n = len(a)
    out = [[0] * n for _ in range(n)]
    macs = 0
    for i0 in range(0, n, tile):
        for j0 in range(0, n, tile):
            for k0 in range(0, n, tile):
                for i in range(i0, min(i0 + tile, n)):
                    for j in range(j0, min(j0 + tile, n)):
                        for k in range(k0, min(k0 + tile, n)):
                            out[i][j] += a[i][k] * b[k][j]
                            macs += 1
    return out, macs


def main():
    random.seed(0)
    a = [[random.randint(0, 3) for _ in range(4)] for _ in range(4)]
    b = [[random.randint(0, 3) for _ in range(4)] for _ in range(4)]
    ref = matmul(a, b)
    out, macs = tiled_matmul(a, b, tile=2)
    print("分块结果与直接矩阵乘一致:", out == ref)
    print("有效 MAC 数:", macs)
    print("要点：分块让权重与输入在阵列内复用，是脉动阵列"
          "降低访存的关键；Gemmini 的配置就是在改这类分块与数据流。")


if __name__ == "__main__":
    main()
