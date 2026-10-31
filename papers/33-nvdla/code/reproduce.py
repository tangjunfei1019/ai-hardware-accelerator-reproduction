"""复现骨架（原创，非原文代码）：NVDLA 式推理流水线。

只用 Python 标准库。演示：卷积（CMAC/CACC 思想）-> ReLU 激活（SDP 思想）
-> 最大池化（PDP 思想），每阶段打印输出尺寸。
运行：python3 reproduce.py
"""


def conv2d(x, k):
    h, w = len(x), len(x[0])
    kh, kw = len(k), len(k[0])
    out = []
    for i in range(h - kh + 1):
        row = []
        for j in range(w - kw + 1):
            row.append(sum(x[i + di][j + dj] * k[di][dj]
                           for di in range(kh) for dj in range(kw)))
        out.append(row)
    return out


def relu(x):
    return [[max(0, v) for v in row] for row in x]


def maxpool2x2(x):
    return [[max(x[i][j], x[i][j + 1], x[i + 1][j], x[i + 1][j + 1])
             for j in range(0, len(x[0]) - 1, 2)]
            for i in range(0, len(x) - 1, 2)]


def main():
    x = [[1, 2, 0, 1], [0, 1, 2, 1], [1, 0, 1, 2], [2, 1, 0, 1]]
    k = [[1, 1], [0, 1]]
    c = conv2d(x, k)
    a = relu(c)
    p = maxpool2x2(a)
    print("输入尺寸:", len(x), "x", len(x[0]))
    print("卷积后:", c, "尺寸:", len(c), "x", len(c[0]))
    print("激活后:", a)
    print("池化后:", p, "尺寸:", len(p), "x", len(p[0]))
    print("要点：NVDLA 的模块化流水线就是把这些阶段串联起来，"
          "融合模式下中间结果不必往返访存。")


if __name__ == "__main__":
    main()
