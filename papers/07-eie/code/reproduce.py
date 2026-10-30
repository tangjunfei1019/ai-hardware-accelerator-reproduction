"""复现骨架（原创，非原文代码）：CSC 稀疏矩阵-向量乘法 + 权重共享。

只用 Python 标准库。演示：只对非零权重做乘法，并通过码本查到真实权重。
运行：python3 reproduce.py
"""


def csc_matvec(values, row_idx, col_ptr, codebook, vec):
    """values: 码本索引；row_idx/col_ptr: CSC 结构；codebook: 索引->真实权重。"""
    n = len(col_ptr) - 1
    out = [0.0] * 100  # 输出长度按最大行号动态扩展，简化处理
    max_row = 0
    for j in range(n):
        if vec[j] == 0:
            continue  # 跳过零激活
        for p in range(col_ptr[j], col_ptr[j + 1]):
            w = codebook[values[p]]
            r = row_idx[p]
            if r >= len(out):
                out.extend([0.0] * (r - len(out) + 1))
            out[r] += w * vec[j]
            max_row = max(max_row, r)
    return out[: max_row + 1]


def main():
    # 矩阵 [[0, 2], [3, 0]] 的 CSC：列0: (行1,值3)；列1: (行0,值2)
    # 码本：索引0->3.0，索引1->2.0
    codebook = [3.0, 2.0]
    values = [0, 1]
    row_idx = [1, 0]
    col_ptr = [0, 1, 2]
    vec = [1.0, 2.0]
    print("矩阵 [[0,2],[3,0]] x [1,2] =", csc_matvec(values, row_idx, col_ptr, codebook, vec))
    print("期望 [4.0, 3.0]；零权重与零激活都被跳过，没有参与乘法。")
    print("权重共享要点：values 存的是码本索引，不是完整浮点权重，存储量随码本大小而非权重数量增长。")


if __name__ == "__main__":
    main()
