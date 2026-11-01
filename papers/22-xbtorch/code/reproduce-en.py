"""Reproduction skeleton (original, not the original authors' code): crossbar MVM + device non-idealities.
Python standard library only. Demonstrates: ideal conductance matrix multiplication vs the result
deviation after quantization + Gaussian noise.
Run: python3 reproduce.py
"""
import random
random.seed(0)

def mvm(weights, x, noise=0.0, levels=16):
    out = []
    for row in weights:
        s = 0.0
        for w, v in zip(row, x):
            q = round(w * (levels - 1)) / (levels - 1)  # Conductance quantization
            q += random.gauss(0, noise)
            s += q * v
        out.append(s)
    return out

def main():
    w = [[0.8, -0.3], [0.2, 0.9]]
    x = [1.0, 2.0]
    print('Ideal output:', mvm(w, x, noise=0.0))
    print('Quantized + noisy output:', [round(v, 3) for v in mvm(w, x, noise=0.05)])
    print('Point: XBTorch\'s value is not in computing this small matrix, but in systematically putting quantization, variation, and noise into the training and inference flow.')

if __name__ == '__main__':
    main()
