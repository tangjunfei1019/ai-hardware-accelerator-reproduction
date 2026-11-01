"""Reproduction skeleton (original, not the paper's code): matrix-vector
multiplication on an analog crossbar array.

Standard library only. Demonstrates the difference between the ideal output,
the output after adding Gaussian noise, and the output after ADC
quantization (4 bit).
Run: python3 reproduce.py
"""

import random


def matvec(weights, x):
    return [sum(w * xi for w, xi in zip(row, x)) for row in weights]


def adc_quantize(values, bits=4):
    """Quantize continuous outputs to 2**bits levels (full scale = max abs value)."""
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
    print("Ideal output:", [round(v, 4) for v in ideal])
    print("After noise:", [round(v, 4) for v in noisy])
    print("After ADC quantization:", [round(v, 4) for v in quantized])
    print("Key point: noise and quantization are the main sources of accuracy "
          "loss in analog compute-in-memory, and hardware-aware training "
          "means modelling them during training.")


if __name__ == "__main__":
    main()
