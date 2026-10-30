"""复现骨架（原创，非原文代码）：PLENA 式扁平阵列与胖 GEMM。

只用 Python 标准库。演示：M、N 很小、K 很大的胖 GEMM 中，
方阵的填充/排空开销占比高，而扁平阵列（沿 K 方向拉长）能
摊薄这部分开销、提升利用率。
运行：python3 reproduce.py
"""


def utilization_square(m, n, k, rows, cols):
    # 输出定驻方阵：输出块大于问题规模时，大量 PE 空闲；再乘填充/排空因子
    busy = (min(m, rows) / rows) * (min(n, cols) / cols)
    return busy * k / (k + rows + cols)


def utilization_flat(m, k, cols):
    # 扁平阵列：行数贴合 M，列沿 K 方向展开做分片规约；
    # K 很大时流水线填满后全部 PE 都有用功，填充开销被 K 摊薄
    return k / (k + cols)


def main():
    m, n, k = 8, 8, 512  # 胖 GEMM：K 远大于 M、N
    square = utilization_square(m, n, k, 16, 16)
    flat = utilization_flat(m, k, 32)  # 同样 256 个 PE，排布为 8 行 x 32 列 K 分片
    print(f"胖 GEMM {m}x{k} x {k}x{n}：方阵 16x16 利用率约 {square:.3f}，扁平 8x32 利用率约 {flat:.3f}")
    assert flat > square
    print("要点：阵列形状要匹配 GEMM 形状——胖 GEMM 配扁平阵列，"
          "填充/排空开销占比下降，利用率自然上升；这就是 PLENA 第一条路径的直觉。")


if __name__ == "__main__":
    main()
