"""复现骨架（原创，非原文代码）：模拟交叉阵列上的矩阵向量乘。

只用 Python 标准库。演示：理想输出、加入高斯噪声后的输出、
以及 ADC 量化（4 bit）后的输出三者之差。
运行：python3 reproduce.py
"""

import random


def matvec(weights, x):
    return [sum(w * xi for w, xi in zip(row, x)) for row in weights]


def adc_quantize(values, bits=4):
    """把连续输出量化到 2**bits 个等级（以最大绝对值为满量程）。"""
    levels = 2 ** bits - 1
    scale = max(abs(v) for v in values) or 1.0
    return [round(v / scale * levels) / levels * scale for v in values]


def main():
    random.seed(0)
    weights = [[0.5, -0.25, 0.75], [0.25, 0.5, -0.5]]
    x = [1.0, 2.0, -1.0]
    ideal = matvec(weights, x)
    noisy = [v + random.gauss(0, 0.05) for v in ideal]
    quantized = adc_quantize(noisy, bits=4)
    print("理想输出:", [round(v, 4) for v in ideal])
    print("加噪声后:", [round(v, 4) for v in noisy])
    print("ADC 量化后:", [round(v, 4) for v in quantized])
    print("要点：噪声与量化是模拟存内计算精度损失的主要来源，"
          "硬件感知训练就是要在训练时把它们建模进去。")


if __name__ == "__main__":
    main()
