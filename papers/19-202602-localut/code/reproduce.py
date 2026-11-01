"""Reproduction skeleton (original, not the original authors' code): LoCaLUT-style lookup packing and deduplication.

Python standard library only. Demonstrates: precomputing the dot product of a weight vector with inputs
as a lookup table, so multiple multiply-accumulates are completed with one lookup;
then canonicalization deduplication of repeated entries.
Run: python3 reproduce.py
"""


def build_lut(weight_vec, input_values):
    # When inputs take a small set of values, dot-product results can be pre-tabulated
    table = {}
    for v in input_values:
        table[v] = sum(w * v for w in weight_vec)
    return table


def canonicalize(table):
    # Canonicalization sketch: keep only one entry per distinct result (deduplication)
    seen, out = set(), {}
    for k, v in table.items():
        if v not in seen:
            seen.add(v)
            out[k] = v
    return out


def main():
    w = [2, 3]
    # Two input scalars looked up separately and then added, as a sketch of one packed dot product
    lut = build_lut(w, [0, 1, 2])
    print("Lookup table (input value -> w dot input sum):", lut)
    assert lut[2] == 2 * (2 + 3)
    dup_table = {0: 0, 1: 5, 2: 10, 3: 5}
    dedup = canonicalize(dup_table)
    print("Entries before deduplication:", len(dup_table), "after:", len(dedup), dedup)
    assert len(dedup) < len(dup_table)
    print("Point: lookup trades multiplication for capacity; once capacity gets expensive, canonicalization deduplication becomes essential — that is the capacity-computation trade-off in LoCaLUT's title.")


if __name__ == "__main__":
    main()
