"""复现骨架（原创，非原文代码）：器件噪声 + ADC 量化对 CIM MVM 的影响。
只用 Python 标准库。演示：理想输出 vs 噪声注入 + 6 位 ADC 量化后的输出偏差。
运行：python3 reproduce.py
"""
import random
random.seed(1)

def adc(x, bits=6):
    levels = 2 ** bits - 1
    return round(max(0.0, min(1.0, x)) * levels) / levels

def main():
    ideal = [0.62, 0.41]
    noisy = [adc(v + random.gauss(0, 0.03)) for v in ideal]
    print('理想:', ideal)
    print('噪声+ADC:', noisy)
    print('要点：NeuroSim V1.5 的价值是把这种噪声、量化与电路 PPA 系统地做到可配置仿真，而不只是算一次偏差。')

if __name__ == '__main__':
    main()
