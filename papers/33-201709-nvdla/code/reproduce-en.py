"""Reproduction skeleton (original, not the paper's code): NVDLA-style
inference pipeline.

Standard library only. Demonstrates: convolution (CMAC/CACC idea) ->
ReLU activation (SDP idea) -> max pooling (PDP idea), printing the output
size at each stage.
Run: python3 reproduce.py
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
    print("Input size:", len(x), "x", len(x[0]))
    print("After convolution:", c, "size:", len(c), "x", len(c[0]))
    print("After activation:", a)
    print("After pooling:", p, "size:", len(p), "x", len(p[0]))
    print("Key point: NVDLA's modular pipeline is exactly chaining these "
          "stages together, and in fused mode intermediate results do not "
          "need to round-trip through memory.")


if __name__ == "__main__":
    main()
