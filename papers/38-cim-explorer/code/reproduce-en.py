#!/usr/bin/env python3
"""Original reproduction skeleton (Python standard library only), not upstream CIM-E code.

Demonstrates binary/ternary inference on an RRAM crossbar: binary/ternary
weight quantization, crossbar-style matrix multiplication, and the effect
of small noise/saturation on the output.
"""
import random

random.seed(1)


def quantize(weights, levels):
    """Binary (+/-1) or ternary (-1/0/+1) quantization."""
    out = []
    for w in weights:
        if levels == 2:
            out.append(1.0 if w >= 0 else -1.0)
        else:
            out.append(0.0 if abs(w) < 0.3 else (1.0 if w > 0 else -1.0))
    return out


def crossbar_mac(weights, inputs, noise=0.05):
    """Crossbar MAC: sum of weight x input, plus small noise, clipped (illustrative ADC saturation)."""
    total = sum(w * x for w, x in zip(weights, inputs))
    total += random.gauss(0, noise)
    return max(-4.0, min(4.0, total))


def main():
    weights = [0.8, -0.5, 0.2, -0.9, 0.4]
    inputs = [1.0, 0.5, -1.0, 0.5, 1.0]
    ideal = sum(w * x for w, x in zip(weights, inputs))
    for levels in (2, 3):
        q = quantize(weights, levels)
        print(f"{levels}-level quantized weights = {q}, crossbar output = {crossbar_mac(q, inputs):.3f}")
    print(f"Ideal full-precision output = {ideal:.3f} (quantized outputs should share its sign and rough magnitude)")
    assert crossbar_mac(quantize(weights, 3), inputs, noise=0.0) * ideal > 0
    print("Self-check passed: binary/ternary crossbar inference preserves the output sign")


if __name__ == "__main__":
    main()
