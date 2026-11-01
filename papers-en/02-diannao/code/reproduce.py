"""Reproduction skeleton (original, not the paper's code): DianNao-style tiled
+ fixed-point NFU computation.

Uses only the Python standard library. Demonstrates: how tiled reuse reduces
repeated weight reads, and the error from 16-bit fixed-point quantization.
Run: python3 reproduce.py
"""
import random


def quantize(x, bits=16):
    """Simple symmetric fixed-point quantization illustration (not the paper's exact format)."""
    scale = 127.0
    q = int(round(x * scale))
    q = max(-scale, min(scale, q))
    return q / scale


def tiled_matmul(a, b, tile=4):
    """Tiled matrix multiplication; returns the result and a weight-read count (simplified accounting)."""
    n, k, m = len(a), len(a[0]), len(b[0])
    out = [[0.0] * m for _ in range(n)]
    reads = 0
    for i0 in range(0, n, tile):
        for j0 in range(0, m, tile):
            # Each tile reads its weight tile once (simplified version of the reuse idea)
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
    print("Tiled result[0][0] =", round(out[0][0], 4))
    print("Tiled weight-tile read accounting =", reads, "(untiled element-wise reads are on the order of 8*8*8 = 512 weight accesses)")
    print("Conclusion: tiling lets the same weight tile be reused many times within a tile, instead of fetching it again for every MAC.")


if __name__ == "__main__":
    main()
