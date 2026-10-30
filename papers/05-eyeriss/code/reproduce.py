"""复现骨架（原创，非原文代码）：Eyeriss 行固定（Row-Stationary）数据流示意。

只用 Python 标准库。演示：一行卷积权重在 PE 内复用，滑窗如何减少重复取数。
运行：python3 reproduce.py
"""


def row_stationary_conv(row, kernel):
    """一行输入与卷积核的滑动乘加，返回输出与乘法次数。"""
    out = []
    macs = 0
    for i in range(len(row) - len(kernel) + 1):
        s = 0
        for j, w in enumerate(kernel):
            s += row[i + j] * w
            macs += 1
        out.append(s)
    return out, macs


def main():
    row = [1, 2, 3, 4, 5, 6]
    kernel = [1, 0, -1]
    out, macs = row_stationary_conv(row, kernel)
    print("输入行:", row)
    print("卷积核:", kernel)
    print("输出:", out, "MAC 数:", macs)
    print("行固定要点：同一行权重在滑窗内被多次复用，权重不必每个输出位置都重新从全局缓冲取一次。")


if __name__ == "__main__":
    main()
