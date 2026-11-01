"""Reproduction skeleton (original, not the original authors' code): the asynchronous pipeline idea of speculative decoding.
Python standard library only. Demonstrates: in synchronous mode, drafting and verification are serial;
in asynchronous mode they overlap and idle time falls.
Run: python3 reproduce.py
"""
def main():
    draft, verify = 2.0, 5.0
    sync = draft + verify
    async_time = max(draft, verify) + 0.5  # Abstraction of switching and control overhead
    print('Synchronous time per round:', sync)
    print('Asynchronous time per round (abstract):', async_time)
    print('Point: AHASD\'s gain comes from task-level decoupling and adaptive draft control, not just from placing two models on two pieces of hardware.')

if __name__ == '__main__':
    main()
