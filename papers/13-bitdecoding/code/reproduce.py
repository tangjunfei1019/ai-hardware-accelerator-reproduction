"""复现骨架（原创，非原文代码）：低比特 KV 缓存量化与注意力。

只用 Python 标准库。演示：4 比特均匀量化 KV、反量化后算注意力分数，
并对比 FP16 与 4 比特的缓存字节数。
运行：python3 reproduce.py
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
    print("原始注意力分数:", ref)
    print("4 比特 KV 反量化后分数:", approx)
    assert all(abs(a - b) < 0.6 for a, b in zip(ref, approx)), "量化误差超出示意范围"
    n = len(flat)
    print(f"KV 缓存字节数：FP16 约 {n * 2} 字节，4 比特约 {n // 2} 字节（未计 scale 等元数据）")
    print("要点：低比特 KV 的收益首先是带宽与容量；只有反量化不成为新瓶颈（张量核心友好布局），加速才能兑现。")


if __name__ == "__main__":
    main()
