"""Reproduction skeleton (original, not the original authors' code): device noise + ADC quantization effects on CIM MVM.
Python standard library only. Demonstrates: ideal output vs output deviation after noise injection + 6-bit ADC quantization.
Run: python3 reproduce.py
"""
import random
random.seed(1)

def adc(x, bits=6):
    levels = 2 ** bits - 1
    return round(max(0.0, min(1.0, x)) * levels) / levels

def main():
    ideal = [0.62, 0.41]
    noisy = [adc(v + random.gauss(0, 0.03)) for v in ideal]
    print('Ideal:', ideal)
    print('Noise + ADC:', noisy)
    print('Point: NeuroSim V1.5\'s value is systematically making this noise, quantization, and circuit PPA configurable simulation, not just computing one deviation.')

if __name__ == '__main__':
    main()
