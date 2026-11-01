"""Reproduction skeleton (original, not the paper's code): crossbar MVM + bit-slicing
+ ADC quantization illustration.

Uses only the Python standard library. Demonstrates: a weight matrix by analogy
with conductance, input voltages by analogy, and output currents as multiply-accumulate.
Run: python3 reproduce.py
"""


def crossbar_mvm(weights, inputs):
    """weights: rows = outputs, columns = inputs; returns each row's multiply-accumulate (current-summation analogy)."""
    return [sum(w * x for w, x in zip(row, inputs)) for row in weights]


def adc_quantize(values, bits=4):
    """ADC quantization illustration: quantize analog outputs to 2^bits levels."""
    levels = (1 << bits) - 1
    mx = max(abs(v) for v in values) or 1.0
    return [round(v / mx * levels) / levels * mx for v in values]


def main():
    weights = [[1, 0, 2], [0, 3, 1]]
    inputs = [1.0, 2.0, 0.5]
    raw = crossbar_mvm(weights, inputs)
    print("Crossbar MVM raw output:", raw, "expected [2.0, 6.5]")
    print("After 4-bit ADC quantization:", [round(v, 3) for v in adc_quantize(raw, bits=4)])
    print("Point: computation completes where data is stored, without moving weights; but ADC resolution directly determines output precision, and is the first bottleneck in compute-in-memory design.")


if __name__ == "__main__":
    main()
