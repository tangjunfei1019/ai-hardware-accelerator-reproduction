"""复现骨架（原创，非原文代码）：PIM roofline 的思想——运算强度决定谁更快。
只用 Python 标准库。演示：低运算强度时带宽受限（PIM 占优），高运算强度时算力受限（CPU/GPU 追上）。
运行：python3 reproduce.py
"""
def main():
    for intensity in (0.1, 1.0, 10.0):
        pim = min(100.0, intensity * 200.0)   # 带宽受限段
        cpu = min(500.0, intensity * 50.0)
        print(f'运算强度 {intensity}: PIM 估计 {pim:.0f}, CPU 估计 {cpu:.0f}')
    print('要点：PIMeval 的价值是系统地找出交叉点，而不是宣称 PIM 在所有强度下都更快。')

if __name__ == '__main__':
    main()
