"""复现骨架（原创，非原文代码）：Focus 式三级流式 token 集中。

只用 Python 标准库。演示：语义剪枝 -> 块级集中 -> 向量去重，
统计每一级剩下的 token 数。
运行：python3 reproduce.py
"""


def semantic_prune(tokens, scores, threshold):
    return [t for t, s in zip(tokens, scores) if s >= threshold]


def block_concentrate(tokens, block_size=2):
    # 块级集中示意：每块取均值向量作为代表
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
    print("原始 token 数:", len(tokens))
    s1 = semantic_prune(tokens, scores, 0.5)
    print("语义剪枝后:", len(s1), s1)
    s2 = block_concentrate(s1)
    print("块级集中后:", len(s2), s2)
    s3 = dedup(s2)
    print("向量去重后:", len(s3), s3)
    assert len(s3) <= len(s2) <= len(s1) <= len(tokens)
    print("要点：三级削减是乘法效应——每一级都在上一级的基础上再压缩，token 越少，后续注意力与 GEMM 的计算量下降越明显。")


if __name__ == "__main__":
    main()
