"""Reproduction skeleton (original, not the original authors' code): the RNS idea — splitting a large integer into small-modulus remainders for separate computation.
Python standard library only. Demonstrates: reconstructing a product with the Chinese remainder
theorem, verifying multiplication equivalence in the remainder domain.
Run: python3 reproduce.py
"""
def crt(rems, mods):
    M = 1
    for m in mods:
        M *= m
    x = 0
    for r, m in zip(rems, mods):
        Mi = M // m
        inv = pow(Mi, -1, m)
        x += r * Mi * inv
    return x % M

def main():
    a, b = 123, 456
    mods = [97, 89, 83]
    ra = [a % m for m in mods]
    rb = [b % m for m in mods]
    rc = [(x * y) % m for x, y, m in zip(ra, rb, mods)]
    print('Direct multiplication:', a * b)
    print('RNS reconstruction:', crt(rc, mods))
    print('Point: DRAMatic uses RNS/NTT to work around weak DPU multiplication and communication bottlenecks; the skeleton only demonstrates the number-theoretic idea and contains no DPU code.')

if __name__ == '__main__':
    main()
