#!/usr/bin/env python3

from pprint import pprint
from bisect import bisect_right
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n_darts, m_score = map(int, input().split())
points = [0]
for _ in range(n_darts):
    p = int(input())
    points.append(p)

# 4本の矢を投げる = 2本の矢をまとめて投げるのを2回行う
# 2本の矢をまとめて投げたときの得点 (矢を投げないことも含む) の合計値を p とする
# 残りの2本の矢を投げたときに得点を q とすると、
# p が与えられたとき、p + q <= M を満たす最大の q を求めればよいことになる

P = []
for i in range(n_darts + 1):
    for j in range(n_darts + 1):
        p = points[i] + points[j]
        P.append(p)
P = sorted(P)
# print(P)

max_score = 0
for p in P:
    if p > max_score:
        continue
    index = bisect_right(P, m_score - p) - 1
    q = P[index]
    max_score = max(max_score, p + q)

print(max_score)
