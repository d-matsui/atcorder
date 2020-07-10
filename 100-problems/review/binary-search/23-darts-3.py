#!/usr/bin/env python3

from pprint import pprint
from bisect import bisect_left
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M = map(int, input().split())
points = [0]
for _ in range(N):
    p = int(input())
    points.append(p)

# まとめて2本の矢を投げ、それを2回行うことを考える
# 2本の矢を投げて得られる点数p_doubleをpoints_doubleとして全列挙する → O(N^2)
# M - p_double を超えない最大の点数を、points_doubleの中から二分探索する → O(logN)
# pを全て試して、最大の点数を求めればよい → O(N^2)

points_double = []
for i in range(N+1):
    for j in range(N+1):
        p_double = points[i] + points[j]
        points_double.append(p_double)
points_double = sorted(points_double)
# pprint(points_double)

res = 0
for p_double in points_double:
    if p_double > M:
        continue
    rest = M - p_double
    idx = bisect_left(points_double, rest) - 1
    # print(f'{res}, {p_double} + {points_double[idx]}')
    res = max(res, p_double + points_double[idx])

print(res)
