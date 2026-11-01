"""Reproduction skeleton (original, not the paper's code): column-granularity
quantization.

Standard library only. Demonstrates: computing a separate scaling factor
for each column of a weight matrix, doing 3-bit quantization and
dequantization, and comparing the error with layer-granularity quantization
that shares one scaling factor for the whole layer.
Run: python3 reproduce.py
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
    # Two columns at very different scales: column granularity should be
    # more accurate than layer granularity.
    weights = [[0.1 * random.random(), 10.0 * random.random()] for _ in range(8)]
    col_q = column_quantize(weights, bits=3)
    flat = [v for row in weights for v in row]
    layer_q_flat = quantize(flat, bits=3)
    layer_q = [layer_q_flat[i * 2:(i + 1) * 2] for i in range(8)]
    print("Column-granularity mean absolute error:",
          round(mean_abs_error(weights, col_q), 4))
    print("Layer-granularity mean absolute error:",
          round(mean_abs_error(weights, layer_q), 4))
    print("Key point: when columns differ greatly in scale, column-granularity "
          "quantization preserves more effective levels for small-scale "
          "columns — exactly ColumnQuant's core idea for ADC and cell-"
          "precision costs.")


if __name__ == "__main__":
    main()
