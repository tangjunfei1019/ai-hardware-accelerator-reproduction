"""复现骨架（原创，非原文代码）：数据搬运记账与三种数据流对比。

只用 Python 标准库。演示：对同一卷积层，改变数据复用方式会如何改变访存量。
运行：python3 reproduce.py
"""
# 假设能耗权重（相对单位，仅用于相对比较，不是真实工艺数字）
COST = {"dram": 100.0, "glb": 10.0, "rf": 1.0}


def estimate(layer, dataflow):
    """layer: (Cin, Cout, H, W, K)。返回各类访问量与相对能耗。"""
    cin, cout, h, w, k = layer
    macs = cin * cout * h * w * k * k
    # 权重、激活、输出的总元素数（简化模型）
    weights = cin * cout * k * k
    acts = cin * h * w
    outs = cout * h * w
    if dataflow == "weight-stationary":
        # 权重留在 PE，激活/输出多搬运
        dram = weights + acts * 4 + outs
        glb = acts * 2 + outs
    elif dataflow == "output-stationary":
        dram = weights * 2 + acts + outs
        glb = weights + acts
    else:  # row-stationary: 行级复用，权重/激活/部分和都在局部复用一部分
        dram = weights + acts + outs
        glb = (weights + acts) // 2 + outs
    rf = macs // 4
    energy = dram * COST["dram"] + glb * COST["glb"] + rf * COST["rf"]
    return {"macs": macs, "dram": dram, "glb": glb, "rf": rf, "energy": energy}


def main():
    layer = (32, 64, 28, 28, 3)
    print("卷积层 (Cin,Cout,H,W,K) =", layer)
    for df in ("weight-stationary", "output-stationary", "row-stationary"):
        r = estimate(layer, df)
        print(f"{df:20s} MACs={r['macs']} DRAM={r['dram']} GLB={r['glb']} 相对能耗={r['energy']:.0f}")
    print("结论：同一算力下，数据流不同，DRAM/GLB 访问量与相对能耗明显不同。")


if __name__ == "__main__":
    main()
