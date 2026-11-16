"""Reproduction skeleton (original, not the original authors' code): the PyPIM idea — tensor operations lowered to in-memory bitwise steps.
Python standard library only. Demonstrates: a small tensor API (create, slice, sum, sort) where each high-level operation is
counted as a sequence of PIM micro-operations, mirroring the upstream README example (x[::2].sum() == 4.75).
The counts are toy estimates, not simulator output.
Run: python3 reproduce.py
"""


class Tensor:
    """A tiny tensor whose operations are lowered to counted PIM micro-ops."""

    total_micro_ops = 0  # shared counter: slices are new Tensors, ops still count

    def __init__(self, values):
        self.values = list(values)

    def __getitem__(self, key):
        return Tensor(self.values[key])

    def sum(self):
        # Bitwise in-memory addition: one micro-op per element added.
        Tensor.total_micro_ops += len(self.values)
        return sum(self.values)

    def sort(self):
        Tensor.total_micro_ops += len(self.values) * 2  # compare + swap passes, toy count
        return Tensor(sorted(self.values))

    def __repr__(self):
        return f"Tensor({self.values})"


def main():
    x = Tensor([0.0, 0.0, 2.5, 1.25, 2.25, 0.0, 0.0, 0.0])
    print(f"x = {x}")
    print(f"x[::2] = {x[::2]}")
    print(f"x[::2].sum() = {x[::2].sum()}  (upstream README example expects 4.75)")
    print(f"x[::2].sort() = {x[::2].sort()}")
    print(f"PIM micro-ops counted for the lowering: {Tensor.total_micro_ops}")
    print("Point: PyPIM lowers ordinary tensor code to PIM micro-operations, so existing Python programs can run on PIM.")


if __name__ == "__main__":
    main()
