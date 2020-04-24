#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

n_vertices, m_edges = map(int, input().split())
edges = [[] for _ in range(n_vertices)]

for _ in range(m_edges):
    x, y = map(int, input().split())
    edges[x - 1].append(y - 1)
# print(edges)

# dp[v] := ノードvを始点としたときの有向パスの長さの最大値
# dp[v] = max(dp[v], rev[v_adj] + 1)


def rec(v):
    if dp[v] != -1:
        # 既に更新済み
        return dp[v]
    for v_adj in edges[v]:
        dp[v] = max(dp[v], rec(v_adj) + 1)
    return dp[v]


dp = [-1 for _ in range(n_vertices)]
res = 0
for v in range(n_vertices):
    res = max(res, rec(v))

print(res + 1)
