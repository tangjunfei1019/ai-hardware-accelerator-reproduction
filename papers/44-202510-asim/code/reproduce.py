"""Reproduction skeleton (original, not the original authors' code): the ASiM idea — analog noise hurts accuracy, majority voting helps.
Python standard library only. Demonstrates: a toy bit-wise MAC with ADC quantization, where adding Gaussian analog noise
degrades the fraction of outputs that stay correct, and repeating each computation 3 times and taking the majority vote
recovers part of the loss — the robustness trade-off ASiM models. Uses a fixed seed so the output is deterministic.
The numbers are toy accuracy proxies, not paper results.
Run: python3 reproduce.py
"""
import random

random.seed(1)

IDEAL = [12, -5, 8, 20, -3, 15, 7, -9, 4, 11]  # toy ideal MAC outputs


def adc_quantize(value, bits=8):
    # Toy ADC: round to the nearest integer step.
    step = 2 ** (bits - 8)
    return round(value / step) * step


def noisy_mac(values, sigma):
    return [adc_quantize(v + random.gauss(0, sigma)) for v in values]


def accuracy(outputs, tolerance=1.5):
    correct = sum(1 for got, want in zip(outputs, IDEAL) if abs(got - want) <= tolerance)
    return correct / len(IDEAL)


def majority_vote(trials):
    voted = []
    for i in range(len(IDEAL)):
        votes = sorted(t[i] for t in trials)
        voted.append(votes[len(votes) // 2])  # median of 3 = majority vote
    return voted


def main():
    clean = [adc_quantize(v) for v in IDEAL]
    print(f"No noise:        accuracy {accuracy(clean):.2f}")
    for sigma in (0.5, 1.0, 2.0):
        noisy = noisy_mac(IDEAL, sigma)
        print(f"Noise sigma={sigma}: accuracy {accuracy(noisy):.2f}")
    voted = majority_vote([noisy_mac(IDEAL, 1.0) for _ in range(3)])
    print(f"Noise sigma=1.0 + 3x majority vote: accuracy {accuracy(voted):.2f}")
    print("Point: even small analog noise degrades ACiM accuracy, and majority voting recovers some of it — ASiM's core trade-off.")


if __name__ == "__main__":
    main()
