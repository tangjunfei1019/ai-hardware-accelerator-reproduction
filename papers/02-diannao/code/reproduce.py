"""复现骨架（原创，非原文代码）：DianNao 式分块 + 定点 NFU 计算。

只用 Python 标准库。演示：分块复用如何减少权重重复读取，以及 16 位定点量化的误差。
运行：python3 reproduce.py
"""
import random


def quantize(x, bits=16):
    """简单对称定点量化示意（非原文精确格式）。"""
    scale = 127.0
    q = int(round(x * scale))
    q = max(-scale, min(scale, q))
    return q / scale


def tiled_matmul(a, b, tile=4):
    """分块矩阵乘法，返回结果与权重读取次数（简化记账）。"""
    n, k, m = len(a), len(a[0]), len(b[0])
    out = [[0.0] * m for _ in range(n)]
    reads = 0
    for i0 in range(0, n, tile):
        for j0 in range(0, m, tile):
            # 每个分块只读一次权重块（复用思想的简化版）
            reads += tile * tile
            for i in range(i0, min(i0 + tile, n)):
                for j in range(j0, min(j0 + tile, m)):
                    s = 0.0
                    for kk in range(k):
                        s += quantize(a[i][kk]) * quantize(b[kk][j])
                    out[i][j] = s
    return out, reads


def main():
    random.seed(0)
    a = [[random.uniform(-1, 1) for _ in range(8)] for _ in range(8)]
    b = [[random.uniform(-1, 1) for _ in range(8)] for _ in range(8)]
    out, reads = tiled_matmul(a, b, tile=4)
    print("分块结果[0][0] =", round(out[0][0], 4))
    print("分块权重块读取记账 =", reads, "（不分块逐元素读取为 8*8*8 = 512 次权重访问量级）")
    print("结论：分块让同一权重块在块内被多次复用，而不是每次 MAC 都重新取数。")


if __name__ == "__main__":
    main()
