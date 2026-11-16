"""Reproduction skeleton (original, not the original authors' code): the CiMLoop statistical energy model idea.
Python standard library only. Demonstrates: exact per-value energy accounting (energy depends on each operand value)
versus a fast statistical model (energy from the average operand value). The statistical estimate is close and far cheaper
to compute — that is the speed/accuracy trade-off CiMLoop's fast model exploits.
The numbers are toy energy units, not paper results.
Run: python3 reproduce.py
"""


def exact_energy(values, base=1.0, per_bit=0.5, per_bit_sq=0.1):
    # Energy grows with the number of set bits actually moved through the circuit,
    # with a nonlinear term: dense operands cost disproportionately more.
    return sum(base + per_bit * bin(v).count("1") + per_bit_sq * bin(v).count("1") ** 2 for v in values)


def statistical_energy(values, base=1.0, per_bit=0.5, per_bit_sq=0.1):
    # Fast model: evaluate the average operand once, scale by count.
    avg_bits = sum(bin(v).count("1") for v in values) / len(values)
    return len(values) * (base + per_bit * avg_bits + per_bit_sq * avg_bits ** 2)


def main():
    values = [3, 7, 12, 5, 9, 14, 2, 11, 6, 13]  # toy operand values
    exact = exact_energy(values)
    fast = statistical_energy(values)
    print(f"Exact per-value energy: {exact:.1f} units (10 evaluations)")
    print(f"Statistical energy:     {fast:.1f} units (1 evaluation)")
    print(f"Relative error: {abs(exact - fast) / exact * 100:.1f}%")
    print("Point: CiMLoop's fast statistical model trades a small error for orders-of-magnitude faster exploration.")


if __name__ == "__main__":
    main()
