"""复现骨架（原创，非原文代码）：向量量化解码——输入×码本点积。

只用 Python 标准库。演示：权重向量被码本索引替代后，
直接算输入与码本的点积，再按索引查表求和，结果应等于反量化后的矩阵乘法。
运行：python3 reproduce.py
"""


def dequant_matmul(x, codebook, indices):
    """先反量化再乘加的参考路径。"""
    out = []
    for row_idx in indices:
        s = 0.0
        for j, code_id in enumerate(row_idx):
            vec = codebook[code_id]
            s += sum(x[k] * vec[k] for k in range(len(x)))
        out.append(s)
    return out


def input_codebook_matmul(x, codebook, indices):
    """EVA 式路径：先算输入与每个码本向量的点积，再按索引查表求和。"""
    dots = [sum(x[k] * vec[k] for k in range(len(x))) for vec in codebook]
    return [sum(dots[c] for c in row_idx) for row_idx in indices]


def main():
    x = [1.0, 2.0]
    codebook = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    # 两行权重，每行由 2 个码本向量拼接而成（索引矩阵）
    indices = [[0, 1], [2, 0]]
    ref = dequant_matmul(x, codebook, indices)
    eva = input_codebook_matmul(x, codebook, indices)
    print("参考路径（反量化后乘加）:", ref)
    print("EVA 路径（输入×码本点积）:", eva)
    assert all(abs(a - b) < 1e-9 for a, b in zip(ref, eva)), "两条路径结果不一致"
    print("要点：码本只需算一次点积（GEMM 形态），多行共享；权重本身只存索引，访存量随索引位宽下降。")


if __name__ == "__main__":
    main()
