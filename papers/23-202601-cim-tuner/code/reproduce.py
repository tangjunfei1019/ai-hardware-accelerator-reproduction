"""Reproduction skeleton (original, not the original authors' code): CIM-Tuner's core idea — hardware-mapping co-search under an area constraint.
Python standard library only. Demonstrates: enumerating macro counts and per-macro capacities, and
selecting the most energy-efficient combination within an area budget.
Run: python3 reproduce.py
"""
def main():
    area_budget = 100
    best = None
    for macros in range(1, 9):
        for cap in (16, 32, 64):
            area = macros * (10 + cap // 8)
            if area > area_budget:
                continue
            # Compute capacity rises with macro count, storage capacity rises with per-macro capacity; imbalance drags the whole down
            score = min(macros * 10, cap) / area
            if best is None or score > best[0]:
                best = (score, macros, cap, area)
    print('Area budget:', area_budget)
    print('Best (score, macro count, per-macro capacity, area):', best)
    print('Point: adding macros without adding storage, or adding storage without adding compute, both waste area through imbalance.')

if __name__ == '__main__':
    main()
