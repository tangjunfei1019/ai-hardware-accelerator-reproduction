"""Reproduction skeleton (original, not the original authors' code): the approximate multiplier accuracy-energy trade-off.
Python standard library only. Demonstrates: truncating low bits saves energy, but error rises with
the number of truncated bits; pick the most energy-saving configuration that satisfies the accuracy constraint.
Run: python3 reproduce.py
"""
def main():
    for trunc in range(0, 5):
        err = (2 ** trunc - 1) / 255.0
        energy = 100 - trunc * 18
        print(f'Truncating {trunc} bits: approximate error about {err:.3f}, relative energy {energy}')
    print('Point: OpenACM\'s work is automating this trade-off, down to transistor-level macros and the physical flow, not just hand-computing a table.')

if __name__ == '__main__':
    main()
