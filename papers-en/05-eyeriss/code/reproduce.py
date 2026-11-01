"""Reproduction skeleton (original, not the paper's code): Eyeriss row-stationary
(Row-Stationary) dataflow illustration.

Uses only the Python standard library. Demonstrates: one row of convolution
weights reused inside a PE, and how a sliding window reduces repeated fetches.
Run: python3 reproduce.py
"""


def row_stationary_conv(row, kernel):
    """Sliding multiply-accumulate of one input row with a kernel; returns the output and MAC count."""
    out = []
    macs = 0
    for i in range(len(row) - len(kernel) + 1):
        s = 0
        for j, w in enumerate(kernel):
            s += row[i + j] * w
            macs += 1
        out.append(s)
    return out, macs


def main():
    row = [1, 2, 3, 4, 5, 6]
    kernel = [1, 0, -1]
    out, macs = row_stationary_conv(row, kernel)
    print("Input row:", row)
    print("Kernel:", kernel)
    print("Output:", out, "MAC count:", macs)
    print("Row-stationary point: the same row weights are reused many times within the sliding window, so weights do not need to be fetched again from the global buffer for every output position.")


if __name__ == "__main__":
    main()
