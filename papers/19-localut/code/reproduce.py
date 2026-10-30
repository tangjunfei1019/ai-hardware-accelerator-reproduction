"""复现骨架（原创，非原文代码）：LoCaLUT 式查表打包与去重。

只用 Python 标准库。演示：把权重向量与输入的点积预先算成查表，
多个乘加一次查表完成；再对重复表项做规范化去重。
运行：python3 reproduce.py
"""


def build_lut(weight_vec, input_values):
    # 输入取值为小集合时，点积结果可预先制表
    table = {}
    for v in input_values:
        table[v] = sum(w * v for w in weight_vec)
    return table


def canonicalize(table):
    # 规范化示意：同一结果只保留一个表项（去重）
    seen, out = set(), {}
    for k, v in table.items():
        if v not in seen:
            seen.add(v)
            out[k] = v
    return out


def main():
    w = [2, 3]
    # 两个输入标量分别查表再相加，等价于一次打包点积的示意
    lut = build_lut(w, [0, 1, 2])
    print("查表（输入值 -> w·输入和）:", lut)
    assert lut[2] == 2 * (2 + 3)
    dup_table = {0: 0, 1: 5, 2: 10, 3: 5}
    dedup = canonicalize(dup_table)
    print("去重前表项:", len(dup_table), "去重后:", len(dedup), dedup)
    assert len(dedup) < len(dup_table)
    print("要点：查表把乘法换成容量；容量一贵，规范化去重就成了必需品——这就是 LoCaLUT 标题里容量-计算权衡的含义。")


if __name__ == "__main__":
    main()
