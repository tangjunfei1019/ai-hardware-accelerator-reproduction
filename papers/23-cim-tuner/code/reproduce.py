"""复现骨架（原创，非原文代码）：CIM-Tuner 的核心思想——面积约束下的硬件-映射协同搜索。
只用 Python 标准库。演示：枚举宏数量与每宏容量，在面积上限内选能效最高的组合。
运行：python3 reproduce.py
"""
def main():
    area_budget = 100
    best = None
    for macros in range(1, 9):
        for cap in (16, 32, 64):
            area = macros * (10 + cap // 8)
            if area > area_budget:
                continue
            # 计算容量随宏数上升，存储容量随单宏容量上升；失衡会拖累整体
            score = min(macros * 10, cap) / area
            if best is None or score > best[0]:
                best = (score, macros, cap, area)
    print('面积预算:', area_budget)
    print('最优（分数, 宏数, 单宏容量, 面积）:', best)
    print('要点：只加宏不加存储，或只加存储不加计算，都会因失衡而浪费面积。')

if __name__ == '__main__':
    main()
