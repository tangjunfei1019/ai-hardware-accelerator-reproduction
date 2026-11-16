"""Reproduction skeleton (original, not the original authors' code): the PIMSIM-NN ISA idea — one instruction stream, many architecture configurations.
Python standard library only. Demonstrates: a tiny ISA (LOAD, MATMUL, VECADD, TRANSFER) is decoded once, then evaluated under two
different core configurations; the same program gives different cycle counts, which is the point of decoupling software from hardware.
The numbers are toy cycle counts, not simulator output.
Run: python3 reproduce.py
"""
# (opcode, cycles per unit) for a small core: scalar / vector / matrix(RRAM crossbar) / transfer
SMALL_CORE = {"LOAD": 2, "MATMUL": 8, "VECADD": 4, "TRANSFER": 6}
BIG_CORE = {"LOAD": 1, "MATMUL": 3, "VECADD": 2, "TRANSFER": 10}  # faster matrix unit, slower NoC

PROGRAM = ["LOAD", "MATMUL", "MATMUL", "VECADD", "TRANSFER", "MATMUL", "VECADD"]


def evaluate(program, core, name):
    total = sum(core[op] for op in program)
    print(f"{name}: total cycles {total} for {len(program)} instructions")
    return total


def main():
    small = evaluate(PROGRAM, SMALL_CORE, "Small core (weak matrix unit)")
    big = evaluate(PROGRAM, BIG_CORE, "Big core (fast matrix unit, slow NoC)")
    print(f"Same program, different architecture: {small} vs {big} cycles.")
    print("Point: PIMSIM-NN's ISA lets one instruction stream be evaluated under many hardware configurations.")


if __name__ == "__main__":
    main()
