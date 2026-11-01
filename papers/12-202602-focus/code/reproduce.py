"""Reproduction skeleton (original, not the original authors' code): Focus-style three-stage streaming token concentration.

Python standard library only. Demonstrates: semantic pruning -> block-level concentration -> vector deduplication,
counting how many tokens remain after each stage.
Run: python3 reproduce.py
"""


def semantic_prune(tokens, scores, threshold):
    return [t for t, s in zip(tokens, scores) if s >= threshold]


def block_concentrate(tokens, block_size=2):
    # Block-level concentration sketch: take the mean vector of each block as its representative
    out = []
    for i in range(0, len(tokens), block_size):
        block = tokens[i:i + block_size]
        dim = len(block[0])
        out.append([sum(v[d] for v in block) / len(block) for d in range(dim)])
    return out


def dedup(tokens, tol=1e-9):
    out = []
    for t in tokens:
        if not any(all(abs(a - b) <= tol for a, b in zip(t, u)) for u in out):
            out.append(t)
    return out


def main():
    tokens = [[1.0, 0.0], [1.0, 0.0], [0.0, 1.0], [0.2, 0.8], [0.0, 1.0], [0.9, 0.1]]
    scores = [0.9, 0.8, 0.3, 0.7, 0.85, 0.6]
    print("Original token count:", len(tokens))
    s1 = semantic_prune(tokens, scores, 0.5)
    print("After semantic pruning:", len(s1), s1)
    s2 = block_concentrate(s1)
    print("After block-level concentration:", len(s2), s2)
    s3 = dedup(s2)
    print("After vector deduplication:", len(s3), s3)
    assert len(s3) <= len(s2) <= len(s1) <= len(tokens)
    print("Point: the three-stage reduction is multiplicative — each stage compresses further on top of the previous one, and fewer tokens means a larger drop in subsequent attention and GEMM compute.")


if __name__ == "__main__":
    main()
