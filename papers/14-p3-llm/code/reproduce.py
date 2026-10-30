"""复现骨架（原创，非原文代码）：P3-LLM 式混合精度与 NPU-PIM 分工。

只用 Python 标准库。演示：权重 4 比特、激活 8 比特的均匀量化，
以及 prefill（算力密集）与解码（访存受限）两种路径的字节量对比。
运行：python3 reproduce.py
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
    print("权重 4 比特反量化:", [round(v, 3) for v in w_q])
    print("激活 8 比特反量化:", [round(v, 3) for v in a_q])
    assert all(abs(a - b) < 0.2 for a, b in zip(weights, w_q))
    # 分工示意：prefill 一次读权重算多个 token（算力密集），解码每 token 都要重读权重（访存受限）
    n_tokens_prefill, n_tokens_decode = 128, 1
    w_bytes = len(weights) * 0.5  # 4 比特
    print(f"权重字节数（4 比特）: {w_bytes}；prefill {n_tokens_prefill} token 摊薄后每 token 约 {w_bytes / n_tokens_prefill:.3f} 字节，"
          f"解码每 token 仍需约 {w_bytes} 字节")
    print("要点：解码访存受限，所以把解码放到 PIM 一侧、把权重压到 4 比特，收益最大；prefill 则留在 NPU 做高密度 GEMM。")


if __name__ == "__main__":
    main()
