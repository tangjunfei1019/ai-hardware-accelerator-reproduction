"""Reproduction skeleton (original, not the original authors' code): PLENA-style flat array and fat GEMM.

Python standard library only. Demonstrates: in a fat GEMM where M and N are small and K is large,
a square array pays a high fill/drain overhead share, while a flat array (stretched along K) can
amortize that overhead and raise utilization.
Run: python3 reproduce.py
"""


def utilization_square(m, n, k, rows, cols):
    # Output-stationary square array: many PEs idle when the output tile is larger than the problem size; then multiply by a fill/drain factor
    busy = (min(m, rows) / rows) * (min(n, cols) / cols)
    return busy * k / (k + rows + cols)


def utilization_flat(m, k, cols):
    # Flat array: rows fit M, columns expand along K for tiled reduction;
    # when K is large, the pipeline fills and all PEs do useful work, so fill overhead is amortized by K
    return k / (k + cols)


def main():
    m, n, k = 8, 8, 512  # Fat GEMM: K far larger than M and N
    square = utilization_square(m, n, k, 16, 16)
    flat = utilization_flat(m, k, 32)  # Same 256 PEs, arranged as 8 rows x 32 columns of K tiles
    print(f"Fat GEMM {m}x{k} x {k}x{n}: square 16x16 utilization about {square:.3f}, flat 8x32 utilization about {flat:.3f}")
    assert flat > square
    print("Point: array shape should match GEMM shape — a fat GEMM with a flat array lowers the "
          "fill/drain overhead share and raises utilization; that is the intuition behind PLENA's first path.")


if __name__ == "__main__":
    main()
