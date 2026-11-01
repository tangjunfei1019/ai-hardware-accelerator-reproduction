"""Reproduction skeleton (original, not the paper's code): small systolic-array-style
matrix multiplication.

Uses only the Python standard library. Demonstrates: weights flowing in column
by column and activations row by row, and how partial sums accumulate in the array.
Run: python3 reproduce.py
"""


def systolic_gemm(a, b):
    """Naive systolic illustration: blocked computation by rows and columns; returns the result, MAC count, and cycles. Real systolic timing is approximated by cycle accounting."""
    n, k, m = len(a), len(a[0]), len(b[0])
    out = [[0] * m for _ in range(n)]
    macs = 0
    cycles = n + m + k  # Fill + compute + drain order-of-magnitude estimate, not real timing
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
    print("A x B =", out, "MAC count:", macs, "cycle order-of-magnitude estimate:", cycles)
    print("Systolic point: data flows and is reused inside the array, instead of every PE repeatedly fetching from memory; the squarer and larger the matrix, the closer utilization gets to peak.")


if __name__ == "__main__":
    main()
