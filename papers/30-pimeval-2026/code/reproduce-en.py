"""Reproduction skeleton (original, not the original authors' code): the PIM roofline idea — arithmetic intensity decides who is faster.
Python standard library only. Demonstrates: at low arithmetic intensity, bandwidth limits performance (PIM wins);
at high intensity, compute limits performance (CPU/GPU catch up).
Run: python3 reproduce.py
"""
def main():
    for intensity in (0.1, 1.0, 10.0):
        pim = min(100.0, intensity * 200.0)   # Bandwidth-limited segment
        cpu = min(500.0, intensity * 50.0)
        print(f'Arithmetic intensity {intensity}: PIM estimate {pim:.0f}, CPU estimate {cpu:.0f}')
    print('Point: PIMeval\'s value is systematically finding the crossover point, not claiming PIM is faster at every intensity.')

if __name__ == '__main__':
    main()
