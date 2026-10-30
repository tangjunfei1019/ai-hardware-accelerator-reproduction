"""复现骨架（原创，非原文代码）：小型脉动阵列式矩阵乘法。

只用 Python 标准库。演示：权重逐列流动、激活逐行流动时，部分和如何在阵列中累积。
运行：python3 reproduce.py
"""


def systolic_gemm(a, b):
    """朴素脉动示意：按行列分块计算，返回结果与 MAC 数。实际脉动时序用 cycle 记账近似。"""
    n, k, m = len(a), len(a[0]), len(b[0])
    out = [[0] * m for _ in range(n)]
    macs = 0
    cycles = n + m + k  # 填充 + 计算 + 排空的量级估计，不是真实时序
    for i in range(n):
        for j in range(m):
            s = 0
            for kk in range(k):
                s += a[i][kk] * b[kk][j]
                macs += 1
            out[i][j] = s
    return out, macs, cycles


def main():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    out, macs, cycles = systolic_gemm(a, b)
    print("A =", a)
    print("B =", b)
    print("A x B =", out, "MAC 数:", macs, "周期量级估计:", cycles)
    print("脉动要点：数据在阵列内流动复用，而不是每个 PE 都从内存重复取数；矩阵越方、越大，利用率越接近峰值。")


if __name__ == "__main__":
    main()
