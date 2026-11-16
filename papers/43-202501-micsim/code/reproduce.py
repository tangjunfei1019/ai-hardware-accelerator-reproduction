"""Reproduction skeleton (original, not the original authors' code): the MICSim statistic-based average mode idea.
Python standard library only. Demonstrates: per-layer exact evaluation (every activation quantized and checked) versus the
average mode (statistics dumped once, then reused for hardware estimation). The average mode is much cheaper and close —
that is the 9-32x speedup MICSim reports against NeuroSim, as a tool comparison.
The numbers are toy estimates, not paper results.
Run: python3 reproduce.py
"""
import time

WEIGHTS = [0.83, -0.41, 0.57, 0.12, -0.66, 0.94, -0.23, 0.38]


def quantize_8bit(values):
    # Toy 8-bit quantization: round to 1/127 steps in [-1, 1].
    return [round(v * 127) / 127 for v in values]


def exact_mode(weights):
    # Evaluate every weight individually (slow, exact).
    return sum(abs(w) for w in quantize_8bit(weights))


def average_mode(weights):
    # Dump statistics once (mean absolute value, non-zero ratio), then reuse them.
    q = quantize_8bit(weights)
    avg_abs = sum(abs(w) for w in q) / len(q)
    nonzero_ratio = sum(1 for w in q if w != 0) / len(q)
    return len(q) * avg_abs, nonzero_ratio


def main():
    t0 = time.perf_counter()
    exact = exact_mode(WEIGHTS)
    t_exact = time.perf_counter() - t0
    t0 = time.perf_counter()
    avg, ratio = average_mode(WEIGHTS)
    t_avg = time.perf_counter() - t0
    print(f"Exact mode:   sum|w| = {exact:.3f} (per-weight evaluation)")
    print(f"Average mode: sum|w| = {avg:.3f}, non-zero ratio = {ratio:.2f} (statistics reused)")
    print(f"Toy timing: exact {t_exact * 1e6:.0f} us vs average {t_avg * 1e6:.0f} us")
    print("Point: MICSim's average mode reuses dumped layer statistics instead of re-evaluating every value.")


if __name__ == "__main__":
    main()
