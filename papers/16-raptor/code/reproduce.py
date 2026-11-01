"""Reproduction skeleton (original, not the original authors' code): 3D-DRAM bandwidth and I/O energy model.

Python standard library only. Demonstrates: for the same number of KV/weight bytes,
how transfer time and I/O energy differ under different bandwidths and pJ/bit values.
Run: python3 reproduce.py
"""


def transfer_time(data_tb, bandwidth_tbps):
    return data_tb / bandwidth_tbps  # seconds (order-of-magnitude sketch)


def io_energy(data_bits, pj_per_bit):
    return data_bits * pj_per_bit * 1e-12  # joules


def main():
    data_tb = 10.0  # sketch: 10 TB of data
    bits = data_tb * 8e12
    for name, bw, pj in [("HBM-style (sketch: 3 TB/s, about 10 pJ/bit)", 3.0, 10.0),
                         ("3D-DRAM-style (sketch: 100 TB/s, 0.37 pJ/bit)", 100.0, 0.37)]:
        t = transfer_time(data_tb, bw)
        e = io_energy(bits, pj)
        print(f"{name}: transfer time about {t:.3f} s, I/O energy about {e:.2f} J")
    assert transfer_time(data_tb, 100.0) < transfer_time(data_tb, 3.0)
    print("Point: the decoding stage of generative inference is bandwidth-bound, and bandwidth density and pJ/bit directly determine latency and energy — that is why Raptor puts DRAM into the 3D package.")


if __name__ == "__main__":
    main()
