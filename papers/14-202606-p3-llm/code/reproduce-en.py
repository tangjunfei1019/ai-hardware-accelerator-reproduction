"""Reproduction skeleton (original, not the original authors' code): P3-LLM-style hybrid precision and NPU-PIM division of labor.

Python standard library only. Demonstrates: 4-bit weights and 8-bit activations with uniform quantization,
and a byte-count comparison between prefill (compute-intensive) and decoding (memory-bound) paths.
Run: python3 reproduce.py
"""


def quantize(values, bits):
    levels = 2 ** bits - 1
    lo, hi = min(values), max(values)
    scale = (hi - lo) / levels if hi > lo else 1.0
    codes = [round((v - lo) / scale) for v in values]
    recon = [lo + c * scale for c in codes]
    return recon


def main():
    weights = [0.3, -1.2, 2.0, 0.8, -0.5, 1.5]
    acts = [0.1, 0.9, -0.4, 1.1]
    w_q = quantize(weights, 4)
    a_q = quantize(acts, 8)
    print("Weights after 4-bit dequantization:", [round(v, 3) for v in w_q])
    print("Activations after 8-bit dequantization:", [round(v, 3) for v in a_q])
    assert all(abs(a - b) < 0.2 for a, b in zip(weights, w_q))
    # Division-of-labor sketch: prefill reads weights once for many tokens (compute-intensive),
    # decoding re-reads weights for every token (memory-bound)
    n_tokens_prefill, n_tokens_decode = 128, 1
    w_bytes = len(weights) * 0.5  # 4-bit
    print(f"Weight bytes (4-bit): {w_bytes}; prefill with {n_tokens_prefill} tokens amortizes to about {w_bytes / n_tokens_prefill:.3f} bytes per token, "
          f"while decoding still needs about {w_bytes} bytes per token")
    print("Point: decoding is memory-bound, so putting decoding on the PIM side and compressing weights to 4 bits gives the largest gain; prefill stays on the NPU for dense GEMM.")


if __name__ == "__main__":
    main()
