"""Reproduction skeleton (original, not the original authors' code): MTIA 300-style communication offloading and overlap.

Python standard library only. Demonstrates: when compute cores also do communication, communication serially
occupies compute time; after offloading to dedicated message engines, communication and compute can overlap,
so total time approaches the maximum of the two rather than their sum.
Run: python3 reproduce.py
"""


def total_time(compute, comm, overlap):
    """overlap is 0..1: the share of communication that can overlap with compute."""
    return compute + comm * (1.0 - overlap)


def main():
    compute, comm = 100.0, 60.0
    serial = total_time(compute, comm, 0.0)
    offloaded = total_time(compute, comm, 0.9)
    print(f"Compute time {compute}, communication time {comm}")
    print(f"Serial (compute cores also doing communication) total time: {serial}")
    print(f"After offloading with 90% overlap total time: {offloaded:.1f}, about {serial / offloaded:.2f}x faster")
    assert offloaded < serial
    print("Point: MTIA 300's gain is not in single-card peak compute, but in removing communication from the compute critical path — "
          "the 12 built-in NICs + 16 message engines serve exactly that goal.")


if __name__ == "__main__":
    main()
