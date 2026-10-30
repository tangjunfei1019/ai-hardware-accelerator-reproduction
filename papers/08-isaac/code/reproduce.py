"""复现骨架（原创，非原文代码）：交叉阵列 MVM + 位切片 + ADC 量化示意。

只用 Python 标准库。演示：权重矩阵以电导类比，输入电压类比，输出电流即乘积累加。
运行：python3 reproduce.py
"""


def crossbar_mvm(weights, inputs):
    """weights: 行=输出，列=输入；返回每行的乘积累加（电流求和类比）。"""
    return [sum(w * x for w, x in zip(row, inputs)) for row in weights]


def adc_quantize(values, bits=4):
    """ADC 量化示意：把模拟输出量化到 2^bits 级。"""
    levels = (1 << bits) - 1
    mx = max(abs(v) for v in values) or 1.0
    return [round(v / mx * levels) / levels * mx for v in values]


def main():
    weights = [[1, 0, 2], [0, 3, 1]]
    inputs = [1.0, 2.0, 0.5]
    raw = crossbar_mvm(weights, inputs)
    print("交叉阵列 MVM 原始输出:", raw, "期望 [2.0, 6.5]")
    print("4 位 ADC 量化后:", [round(v, 3) for v in adc_quantize(raw, bits=4)])
    print("要点：计算在存储位置完成，不搬权重；但 ADC 分辨率直接决定输出精度，是存算一体设计的第一瓶颈。")


if __name__ == "__main__":
    main()
