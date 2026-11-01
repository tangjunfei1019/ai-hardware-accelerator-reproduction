"""Reproduction skeleton (original, not the paper's code): tiny domain-specific
instruction interpreter.

Uses only the Python standard library. Instruction set illustration: LOAD, MATMUL,
RELU, POOL, demonstrating that the same primitives express different operators.
Run: python3 reproduce.py
"""


def run(program, mem):
    """program: list of instructions; mem: register/storage dictionary. Returns mem."""
    for ins in program:
        op = ins[0]
        if op == "LOAD":
            _, dst, value = ins
            mem[dst] = value
        elif op == "MATMUL":
            _, dst, a, b = ins
            aa, bb = mem[a], mem[b]
            mem[dst] = [[sum(aa[i][k] * bb[k][j] for k in range(len(bb)))
                         for j in range(len(bb[0]))] for i in range(len(aa))]
        elif op == "RELU":
            _, dst, src = ins
            mem[dst] = [[max(0, x) for x in row] for row in mem[src]]
        elif op == "POOL":
            _, dst, src = ins
            srcm = mem[src]
            mem[dst] = [[max(srcm[i][j], srcm[i][j + 1], srcm[i + 1][j], srcm[i + 1][j + 1])
                         for j in range(0, len(srcm[0]), 2)] for i in range(0, len(srcm), 2)]
        else:
            raise ValueError(f"Unknown instruction {op}")
    return mem


def main():
    mem = {}
    prog = [
        ("LOAD", "A", [[1, -2], [3, 4]]),
        ("LOAD", "B", [[1, 0], [0, 1]]),
        ("MATMUL", "C", "A", "B"),
        ("RELU", "D", "C"),
        ("POOL", "E", "D"),
    ]
    out = run(prog, mem)
    print("MATMUL result C =", out["C"])
    print("RELU result D =", out["D"])
    print("POOL result E =", out["E"], "(2x2 pooling to 1x1)")
    print("Point: the same set of vector/matrix primitives can be combined to express fully-connected, activation, pooling, and other operators — that is the value of a domain-specific ISA.")


if __name__ == "__main__":
    main()
