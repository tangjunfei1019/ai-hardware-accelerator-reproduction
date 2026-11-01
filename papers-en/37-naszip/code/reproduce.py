#!/usr/bin/env python3
"""Original reproduction skeleton (Python standard library only), not upstream NasZip code.

Demonstrates feature-level early exiting in approximate nearest-neighbor
search: estimate the full-dimensional distance from a prefix of dimensions,
and prune early when the estimate is already large enough.
"""
import math, random

random.seed(0)


def full_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def early_exit_distance(a, b, prefix_dims, threshold):
    """Estimate the full distance from the first prefix_dims dimensions; exit early if it exceeds the threshold."""
    partial = sum((x - y) ** 2 for x, y in zip(a[:prefix_dims], b[:prefix_dims]))
    # Scale the estimate by the dimension ratio (illustrative model, not the paper's PCA estimate)
    estimate = math.sqrt(partial * len(a) / prefix_dims)
    exited = estimate > threshold
    return estimate, exited


def main():
    dim = 16
    query = [random.gauss(0, 1) for _ in range(dim)]
    candidates = [[random.gauss(0, 1) for _ in range(dim)] for _ in range(20)]
    # Far candidate: shifted away so it can be pruned early
    far = [x + 3.0 for x in query]
    candidates.append(far)
    threshold = 3.0
    saved = 0
    for cand in candidates:
        est, exited = early_exit_distance(query, cand, prefix_dims=4, threshold=threshold)
        if exited:
            saved += dim - 4
    print(f"Candidates = {len(candidates)}, dimension computations saved by early exit = {saved}")
    print(f"Far candidate full distance = {full_distance(query, far):.2f}, 4-dim estimate = {early_exit_distance(query, far, 4, threshold)[0]:.2f}, should be pruned")
    assert early_exit_distance(query, far, 4, threshold)[1]
    print("Self-check passed: early exit can prune a far candidate without computing all dimensions")


if __name__ == "__main__":
    main()
