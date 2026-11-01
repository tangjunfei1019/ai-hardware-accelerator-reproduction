"""Reproduction skeleton (original, not the paper's code): compressed sparse
convolution + scatter accumulation.

Uses only the Python standard library. Demonstrates: multiplying only nonzero
weights/activations, and accumulating products by coordinate to the output.
Run: python3 reproduce.py
"""


def sparse_conv(act, weights):
    """act: sparse input dict {(h,w): value}; weights: sparse weight dict {(kh,kw): value}.
    Returns the output dict and the effective MAC count."""
    out = {}
    macs = 0
    for (h, w), av in act.items():
        if av == 0:
            continue
        for (kh, kw), wv in weights.items():
            if wv == 0:
                continue
            key = (h + kh, w + kw)
            out[key] = out.get(key, 0) + av * wv
            macs += 1
    return out, macs


def main():
    act = {(0, 0): 1.0, (0, 2): 2.0, (1, 1): 3.0}
    weights = {(0, 0): 1.0, (0, 1): 0.0, (1, 0): 2.0}
    out, macs = sparse_conv(act, weights)
    print("Sparse input:", act)
    print("Sparse weights:", weights)
    print("Sparse convolution output:", out)
    print("Effective MAC count:", macs, "(a dense approach would multiply all position combinations without skipping zero values, and its effective MAC count would be clearly larger)")
    print("Point: scatter accumulation correctly places products from irregular positions, and it is the step most easily gotten wrong when reproducing sparse convolution.")


if __name__ == "__main__":
    main()
