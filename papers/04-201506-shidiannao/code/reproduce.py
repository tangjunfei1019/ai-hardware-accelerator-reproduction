"""Reproduction skeleton (original, not the paper's code): ShiDianNao-style
sensor-direct vs. via-DRAM paths.

Uses only the Python standard library. Demonstrates: the DRAM accesses saved
by a direct connection when a small model fits in on-chip SRAM.
Run: python3 reproduce.py
"""


def accesses(model_bytes, sram_bytes, image_bytes, via_dram=True):
    """Returns DRAM access bytes (simplified accounting)."""
    if via_dram:
        return model_bytes + image_bytes * 2  # Written to DRAM, then read back
    if model_bytes <= sram_bytes:
        return 0  # Model is on chip, image goes directly into compute
    return model_bytes - sram_bytes  # Model does not fit; the overflow still goes via DRAM


def main():
    for model in (1_000_000, 10_000_000, 100_000_000):
        d = accesses(model, 2_000_000, 1_000_000, True)
        s = accesses(model, 2_000_000, 1_000_000, False)
        print(f"model={model} bytes  via DRAM={d}  direct={s}  saved={d-s}")
    print("Conclusion: the smaller the model, and the better it fits in on-chip SRAM, the larger the direct-connection benefit; when the model is too large, the benefit decays.")


if __name__ == "__main__":
    main()
