"""复现骨架（原创，非原文代码）：交叉阵列 MVM + 器件非理想性。
只用 Python 标准库。演示：理想电导矩阵乘法 vs 量化 + 高斯噪声后的结果偏差。
运行：python3 reproduce.py
"""
import random
random.seed(0)

def mvm(weights, x, noise=0.0, levels=16):
    out = []
    for row in weights:
        s = 0.0
        for w, v in zip(row, x):
            q = round(w * (levels - 1)) / (levels - 1)  # 电导量化
            q += random.gauss(0, noise)
            s += q * v
        out.append(s)
    return out

def main():
    w = [[0.8, -0.3], [0.2, 0.9]]
    x = [1.0, 2.0]
    print('理想输出:', mvm(w, x, noise=0.0))
    print('量化+噪声输出:', [round(v, 3) for v in mvm(w, x, noise=0.05)])
    print('要点：XBTorch 的价值不在算出这个小矩阵，而在把量化、变异、噪声系统地放进训练与推理流程。')

if __name__ == '__main__':
    main()
