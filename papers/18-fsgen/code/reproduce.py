"""复现骨架（原创，非原文代码）：FSGen 式融合 + 稀疏收益模型。

只用 Python 标准库。演示：稀疏跳过零值 MAC，融合跳过中间结果的
片外写回与重读，两者叠加后的访存与计算削减。
运行：python3 reproduce.py
"""


def fused_sparse_stats(matrix, fused=True):
    total = sum(len(row) for row in matrix)
    nonzero = sum(1 for row in matrix for v in row if v != 0)
    # 未融合：每个算子都要把中间结果写回片外再读回，流量按 2 倍计；融合后只计 1 倍
    traffic = nonzero * (1 if fused else 2)
    return {"total": total, "nonzero_macs": nonzero, "traffic_units": traffic}


def main():
    mat = [[0, 2, 0, 0], [3, 0, 0, 1], [0, 0, 0, 0], [4, 0, 5, 0]]
    dense = fused_sparse_stats([[1] * 4 for _ in range(4)], fused=False)
    sparse_fused = fused_sparse_stats(mat, fused=True)
    sparse_only = fused_sparse_stats(mat, fused=False)
    print("稠密未融合:", dense)
    print("稀疏未融合:", sparse_only)
    print("稀疏 + 融合:", sparse_fused)
    assert sparse_fused["nonzero_macs"] < dense["total"]
    assert sparse_fused["traffic_units"] < sparse_only["traffic_units"]
    print("要点：稀疏省的是计算量，融合省的是访存量；FSGen 的生成器就是让这两种数据流可以按配置组合生成，而不是每次手写。")


if __name__ == "__main__":
    main()
