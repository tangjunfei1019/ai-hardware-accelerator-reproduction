"""复现骨架（原创，非原文代码）：微型领域专用指令解释器。

只用 Python 标准库。指令集示意：LOAD、MATMUL、RELU、POOL，演示同一套原语表达不同算子。
运行：python3 reproduce.py
"""


def run(program, mem):
    """program: 指令列表；mem: 寄存器/存储字典。返回 mem。"""
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
            raise ValueError(f"未知指令 {op}")
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
    print("MATMUL 结果 C =", out["C"])
    print("RELU 结果 D =", out["D"])
    print("POOL 结果 E =", out["E"], "（2x2 池化为 1x1）")
    print("要点：同一套向量/矩阵原语可以组合表达全连接、激活、池化等不同算子，这就是领域专用 ISA 的价值。")


if __name__ == "__main__":
    main()
