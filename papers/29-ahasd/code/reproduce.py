"""复现骨架（原创，非原文代码）：推测解码的异步流水思想。
只用 Python 标准库。演示：同步模式下草稿与验证串行，异步模式下两者重叠，空闲减少。
运行：python3 reproduce.py
"""
def main():
    draft, verify = 2.0, 5.0
    sync = draft + verify
    async_time = max(draft, verify) + 0.5  # 切换与控制开销的抽象
    print('同步每轮时间:', sync)
    print('异步每轮时间（抽象）:', async_time)
    print('要点：AHASD 的收益来自任务级解耦与自适应草稿控制，而不只是把两个模型放在两个硬件上。')

if __name__ == '__main__':
    main()
