"""复现骨架（原创，非原文代码）：压缩稀疏卷积 + 散射累加。

只用 Python 标准库。演示：只对非零权重/激活做乘法，乘积按坐标散射累加到输出。
运行：python3 reproduce.py
"""


def sparse_conv(act, weights):
    """act: 稀疏输入字典 {(h,w):值}；weights: 稀疏权重字典 {(kh,kw):值}。
    返回输出字典与有效 MAC 数。"""
    out = {}
    macs = 0
    for (h, w), av in act.items():
        if av == 0:
            continue
        for (kh, kw), wv in weights.items():
            if wv == 0:
                continue
            key = (h + kh, w + kw)
            out[key] = out.get(key, 0) + av * wv
            macs += 1
    return out, macs


def main():
    act = {(0, 0): 1.0, (0, 2): 2.0, (1, 1): 3.0}
    weights = {(0, 0): 1.0, (0, 1): 0.0, (1, 0): 2.0}
    out, macs = sparse_conv(act, weights)
    print("稀疏输入:", act)
    print("稀疏权重:", weights)
    print("稀疏卷积输出:", out)
    print("有效 MAC 数:", macs, "（稠密做法会对所有位置组合做乘法且不跳过零值，有效 MAC 数会明显更多）")
    print("要点：散射累加把不规则位置的乘积正确归位，是稀疏卷积复现中最容易出错的一步。")


if __name__ == "__main__":
    main()
