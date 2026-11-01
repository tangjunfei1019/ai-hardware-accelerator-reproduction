"""Reproduction skeleton (original, not the paper's code): systolic-array-style
tiled matrix multiplication.

Standard library only. Demonstrates: splitting matrix multiplication into
2x2 tiles, computing local products per tile and accumulating them, giving
the same result as direct matrix multiplication, while counting effective
multiplications.
Run: python3 reproduce.py
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
    print("Tiled result matches direct matrix multiplication:", out == ref)
    print("Effective MAC count:", macs)
    print("Key point: tiling lets weights and inputs be reused inside the "
          "array, which is how a systolic array cuts memory traffic; "
          "Gemmini's configuration is about changing this kind of tiling "
          "and dataflow.")


if __name__ == "__main__":
    main()
