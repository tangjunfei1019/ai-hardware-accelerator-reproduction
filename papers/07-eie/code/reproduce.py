"""Reproduction skeleton (original, not the paper's code): CSC sparse matrix-vector
multiplication + weight sharing.

Uses only the Python standard library. Demonstrates: multiplying only by nonzero
weights, and looking up real weights through a codebook.
Run: python3 reproduce.py
"""


def csc_matvec(values, row_idx, col_ptr, codebook, vec):
    """values: codebook indices; row_idx/col_ptr: CSC structure; codebook: index -> real weight."""
    n = len(col_ptr) - 1
    out = [0.0] * 100  # Output length is extended dynamically by max row index, simplified handling
    max_row = 0
    for j in range(n):
        if vec[j] == 0:
            continue  # Skip zero activations
        for p in range(col_ptr[j], col_ptr[j + 1]):
            w = codebook[values[p]]
            r = row_idx[p]
            if r >= len(out):
                out.extend([0.0] * (r - len(out) + 1))
            out[r] += w * vec[j]
            max_row = max(max_row, r)
    return out[: max_row + 1]


def main():
    # Matrix [[0, 2], [3, 0]] in CSC: column 0: (row 1, value 3); column 1: (row 0, value 2)
    # Codebook: index 0 -> 3.0, index 1 -> 2.0
    codebook = [3.0, 2.0]
    values = [0, 1]
    row_idx = [1, 0]
    col_ptr = [0, 1, 2]
    vec = [1.0, 2.0]
    print("Matrix [[0,2],[3,0]] x [1,2] =", csc_matvec(values, row_idx, col_ptr, codebook, vec))
    print("Expected [4.0, 3.0]; zero weights and zero activations were skipped and did not take part in multiplication.")
    print("Weight-sharing point: values store codebook indices, not full floating-point weights, so storage grows with codebook size rather than weight count.")


if __name__ == "__main__":
    main()
