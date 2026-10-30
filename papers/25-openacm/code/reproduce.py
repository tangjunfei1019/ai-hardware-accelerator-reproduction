"""复现骨架（原创，非原文代码）：近似乘法器的精度-能量权衡。
只用 Python 标准库。演示：截断低位可省能量，但误差随截断位数上升；选满足精度约束的最省能量配置。
运行：python3 reproduce.py
"""
def main():
    for trunc in range(0, 5):
        err = (2 ** trunc - 1) / 255.0
        energy = 100 - trunc * 18
        print(f'截断 {trunc} 位: 近似误差约 {err:.3f}, 相对能量 {energy}')
    print('要点：OpenACM 的工作是把这种权衡自动化，并做到晶体管级宏与物理流程，而不只是手算一张表。')

if __name__ == '__main__':
    main()
