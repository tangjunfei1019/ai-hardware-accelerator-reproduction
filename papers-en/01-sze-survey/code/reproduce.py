"""Reproduction skeleton (original, not the paper's code): data-movement accounting
and a comparison of three dataflows.

Uses only the Python standard library. Demonstrates: for the same convolutional
layer, how changing the data-reuse pattern changes memory accesses.
Run: python3 reproduce.py
"""
# Assumed energy weights (relative units, for relative comparison only,
# not real process numbers)
COST = {"dram": 100.0, "glb": 10.0, "rf": 1.0}


def estimate(layer, dataflow):
    """layer: (Cin, Cout, H, W, K). Returns access counts and relative energy."""
    cin, cout, h, w, k = layer
    macs = cin * cout * h * w * k * k
    # Total element counts for weights, activations, and outputs (simplified model)
    weights = cin * cout * k * k
    acts = cin * h * w
    outs = cout * h * w
    if dataflow == "weight-stationary":
        # Weights stay in the PEs; activations/outputs move more
        dram = weights + acts * 4 + outs
        glb = acts * 2 + outs
    elif dataflow == "output-stationary":
        dram = weights * 2 + acts + outs
        glb = weights + acts
    else:  # row-stationary: row-level reuse, weights/activations/partial sums
        # are each partly reused locally
        dram = weights + acts + outs
        glb = (weights + acts) // 2 + outs
    rf = macs // 4
    energy = dram * COST["dram"] + glb * COST["glb"] + rf * COST["rf"]
    return {"macs": macs, "dram": dram, "glb": glb, "rf": rf, "energy": energy}


def main():
    layer = (32, 64, 28, 28, 3)
    print("Convolutional layer (Cin,Cout,H,W,K) =", layer)
    for df in ("weight-stationary", "output-stationary", "row-stationary"):
        r = estimate(layer, df)
        print(f"{df:20s} MACs={r['macs']} DRAM={r['dram']} GLB={r['glb']} relative energy={r['energy']:.0f}")
    print("Conclusion: at the same compute power, different dataflows give clearly different DRAM/GLB accesses and relative energy.")


if __name__ == "__main__":
    main()
