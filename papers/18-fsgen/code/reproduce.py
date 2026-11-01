"""Reproduction skeleton (original, not the original authors' code): FSGen-style fusion + sparsity gain model.

Python standard library only. Demonstrates: sparsity skips zero-valued MACs, fusion skips the
off-chip write-back and re-read of intermediate results, and the two together cut traffic and compute.
Run: python3 reproduce.py
"""


def fused_sparse_stats(matrix, fused=True):
    total = sum(len(row) for row in matrix)
    nonzero = sum(1 for row in matrix for v in row if v != 0)
    # Unfused: each operator writes intermediates off-chip and reads them back, so traffic counts 2x; fused counts 1x
    traffic = nonzero * (1 if fused else 2)
    return {"total": total, "nonzero_macs": nonzero, "traffic_units": traffic}


def main():
    mat = [[0, 2, 0, 0], [3, 0, 0, 1], [0, 0, 0, 0], [4, 0, 5, 0]]
    dense = fused_sparse_stats([[1] * 4 for _ in range(4)], fused=False)
    sparse_fused = fused_sparse_stats(mat, fused=True)
    sparse_only = fused_sparse_stats(mat, fused=False)
    print("Dense, unfused:", dense)
    print("Sparse, unfused:", sparse_only)
    print("Sparse + fused:", sparse_fused)
    assert sparse_fused["nonzero_macs"] < dense["total"]
    assert sparse_fused["traffic_units"] < sparse_only["traffic_units"]
    print("Point: sparsity saves compute, fusion saves memory traffic; FSGen's generator lets these two dataflows be combined by configuration instead of hand-writing them each time.")


if __name__ == "__main__":
    main()
