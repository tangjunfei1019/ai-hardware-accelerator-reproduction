#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原创复现骨架（仅 Python 标准库），不是上游 NasZip 代码。

演示近似最近邻搜索中的特征级提前退出思想：先用部分维度
估计全维距离，若估计已足够大则提前剪枝，避免算满全部维度。
"""
import math, random

random.seed(0)


def full_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def early_exit_distance(a, b, prefix_dims, threshold):
    """用前 prefix_dims 维估计全维距离；估计值超过阈值则提前退出。"""
    partial = sum((x - y) ** 2 for x, y in zip(a[:prefix_dims], b[:prefix_dims]))
    # 按维度比例放大估计（示意模型，非原文 PCA 估计）
    estimate = math.sqrt(partial * len(a) / prefix_dims)
    exited = estimate > threshold
    return estimate, exited


def main():
    dim = 16
    query = [random.gauss(0, 1) for _ in range(dim)]
    candidates = [[random.gauss(0, 1) for _ in range(dim)] for _ in range(20)]
    # 远候选：人为拉远，使其可被提前剪枝
    far = [x + 3.0 for x in query]
    candidates.append(far)
    threshold = 3.0
    saved = 0
    for cand in candidates:
        est, exited = early_exit_distance(query, cand, prefix_dims=4, threshold=threshold)
        if exited:
            saved += dim - 4
    print(f"候选数 = {len(candidates)}，提前退出节省的维度计算 = {saved}")
    print(f"远候选全维距离 = {full_distance(query, far):.2f}，4 维估计 = {early_exit_distance(query, far, 4, threshold)[0]:.2f}，应被剪枝")
    assert early_exit_distance(query, far, 4, threshold)[1]
    print("自检通过：提前退出可在不算满维度的情况下剪掉远候选")


if __name__ == "__main__":
    main()
