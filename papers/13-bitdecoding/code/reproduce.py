"""Reproduction skeleton (original, not the original authors' code): low-bit KV cache quantization and attention.

Python standard library only. Demonstrates: 4-bit uniform quantization of KV, attention scores after
dequantization, and a comparison of FP16 vs 4-bit cache byte counts.
Run: python3 reproduce.py
"""


def quantize_4bit(values):
    lo, hi = min(values), max(values)
    scale = (hi - lo) / 15.0 if hi > lo else 1.0
    codes = [round((v - lo) / scale) for v in values]
    return codes, lo, scale


def dequantize(codes, lo, scale):
    return [lo + c * scale for c in codes]


def attention_scores(query, keys):
    return [sum(q * k for q, k in zip(query, key)) for key in keys]


def main():
    keys = [[1.0, 2.0], [0.5, -1.0], [2.0, 0.0]]
    query = [1.0, 0.5]
    flat = [v for row in keys for v in row]
    codes, lo, scale = quantize_4bit(flat)
    recon = dequantize(codes, lo, scale)
    keys_q = [recon[i * 2:(i + 1) * 2] for i in range(len(keys))]
    ref = attention_scores(query, keys)
    approx = attention_scores(query, keys_q)
    print("Original attention scores:", ref)
    print("Scores after 4-bit KV dequantization:", approx)
    assert all(abs(a - b) < 0.6 for a, b in zip(ref, approx)), "Quantization error exceeds the sketch range"
    n = len(flat)
    print(f"KV cache bytes: FP16 about {n * 2} bytes, 4-bit about {n // 2} bytes (excluding scale and other metadata)")
    print("Point: the gain of low-bit KV starts with bandwidth and capacity; speedup only materializes if dequantization does not become the new bottleneck (a tensor-core-friendly layout).")


if __name__ == "__main__":
    main()
