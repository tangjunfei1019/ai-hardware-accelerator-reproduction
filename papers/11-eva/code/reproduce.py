"""Reproduction skeleton (original, not the original authors' code): vector-quantized decoding — input x codebook dot product.

Python standard library only. Demonstrates: after weight vectors are replaced by codebook indices,
computing the input's dot product with the codebook directly and summing by index gives the same
result as dequantized matrix multiplication.
Run: python3 reproduce.py
"""


def dequant_matmul(x, codebook, indices):
    """Reference path: dequantize first, then multiply-accumulate."""
    out = []
    for row_idx in indices:
        s = 0.0
        for j, code_id in enumerate(row_idx):
            vec = codebook[code_id]
            s += sum(x[k] * vec[k] for k in range(len(x)))
        out.append(s)
    return out


def input_codebook_matmul(x, codebook, indices):
    """EVA-style path: compute the input's dot product with each codebook vector first, then sum by index."""
    dots = [sum(x[k] * vec[k] for k in range(len(x))) for vec in codebook]
    return [sum(dots[c] for c in row_idx) for row_idx in indices]


def main():
    x = [1.0, 2.0]
    codebook = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    # Two weight rows, each formed by concatenating 2 codebook vectors (index matrix)
    indices = [[0, 1], [2, 0]]
    ref = dequant_matmul(x, codebook, indices)
    eva = input_codebook_matmul(x, codebook, indices)
    print("Reference path (dequantize then multiply-accumulate):", ref)
    print("EVA path (input x codebook dot product):", eva)
    assert all(abs(a - b) < 1e-9 for a, b in zip(ref, eva)), "The two paths disagree"
    print("Point: the codebook dot products need only be computed once (GEMM form) and are shared across rows; weights themselves store only indices, so memory traffic falls with index bit-width.")


if __name__ == "__main__":
    main()
