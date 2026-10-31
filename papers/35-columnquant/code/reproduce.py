"""复现骨架（原创，非原文代码）：列粒度量化。

只用 Python 标准库。演示：对权重矩阵的每一列单独算缩放因子，
做 3-bit 量化再反量化，并与整层共用一个缩放因子的
层粒度量化比较误差。
运行：python3 reproduce.py
"""

import random


def quantize(values, bits=3):
    levels = 2 ** bits - 1
    scale = max(abs(v) for v in values) or 1.0
    return [round(v / scale * levels) / levels * scale for v in values]


def column_quantize(matrix, bits=3):
    cols = list(zip(*matrix))
    qcols = [quantize(list(col), bits) for col in cols]
    return [list(row) for row in zip(*qcols)]


def mean_abs_error(a, b):
    flat_a = [v for row in a for v in row]
    flat_b = [v for row in b for v in row]
    return sum(abs(x - y) for x, y in zip(flat_a, flat_b)) / len(flat_a)


def main():
    random.seed(0)
    # 两列量级明显不同：列粒度应比层粒度更准确。
    weights = [[0.1 * random.random(), 10.0 * random.random()] for _ in range(8)]
    col_q = column_quantize(weights, bits=3)
    flat = [v for row in weights for v in row]
    layer_q_flat = quantize(flat, bits=3)
    layer_q = [layer_q_flat[i * 2:(i + 1) * 2] for i in range(8)]
    print("列粒度平均绝对误差:", round(mean_abs_error(weights, col_q), 4))
    print("层粒度平均绝对误差:", round(mean_abs_error(weights, layer_q), 4))
    print("要点：当各列量级差异大时，列粒度量化能给小量级列"
          "保留更多有效等级，这正是 ColumnQuant 针对 ADC 与"
          "单元精度成本的核心思想。")


if __name__ == "__main__":
    main()
