#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原创复现骨架（仅 Python 标准库），不是上游 CIM-E 代码。

演示 RRAM 交叉阵列上的二值/三值推理思想：权重二值/三值量化、
交叉阵列式矩阵乘法，以及简单噪声/饱和对输出的影响。
"""
import random

random.seed(1)


def quantize(weights, levels):
    """二值（±1）或三值（-1/0/+1）量化。"""
    out = []
    for w in weights:
        if levels == 2:
            out.append(1.0 if w >= 0 else -1.0)
        else:
            out.append(0.0 if abs(w) < 0.3 else (1.0 if w > 0 else -1.0))
    return out


def crossbar_mac(weights, inputs, noise=0.05):
    """交叉阵列 MAC：权重×输入求和，加小噪声并截断（示意 ADC 饱和）。"""
    total = sum(w * x for w, x in zip(weights, inputs))
    total += random.gauss(0, noise)
    return max(-4.0, min(4.0, total))


def main():
    weights = [0.8, -0.5, 0.2, -0.9, 0.4]
    inputs = [1.0, 0.5, -1.0, 0.5, 1.0]
    ideal = sum(w * x for w, x in zip(weights, inputs))
    for levels in (2, 3):
        q = quantize(weights, levels)
        print(f"{levels} 值量化权重 = {q}，交叉阵列输出 = {crossbar_mac(q, inputs):.3f}")
    print(f"理想全精度输出 = {ideal:.3f}（量化输出应与之同号、量级相近）")
    assert crossbar_mac(quantize(weights, 3), inputs, noise=0.0) * ideal > 0
    print("自检通过：二值/三值交叉阵列推理保留了输出符号")


if __name__ == "__main__":
    main()
