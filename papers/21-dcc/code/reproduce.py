"""复现骨架（原创，非原文代码）：DCC 的核心思想——数据布局决定 PIM 收益。
只用 Python 标准库。演示：同一矩阵分块，主机连续布局与 PIM 本地 bank 布局的重排代价不同；
把分片策略与计算循环分片对齐后，重排量下降。
运行：python3 reproduce.py
"""
def rearrangement_cost(rows, banks, layout):
    # layout='host': 连续元素跨 bank，PIM 计算前需重排；'pim': 连续元素已在本地 bank
    if layout == 'host':
        return rows * (banks - 1)
    return rows // banks

def main():
    rows, banks = 1024, 8
    host = rearrangement_cost(rows, banks, 'host')
    pim = rearrangement_cost(rows, banks, 'pim')
    print('主机布局重排代价（相对单位）:', host)
    print('PIM 本地布局重排代价（相对单位）:', pim)
    print('对齐后重排下降倍数: %.2f' % (host / max(pim, 1)))
    print('要点：DCC 不是只优化计算，而是把数据分片映射为计算循环分片，联合优化重排与计算。')

if __name__ == '__main__':
    main()
