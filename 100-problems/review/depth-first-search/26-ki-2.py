#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
# pprint(tree)
queries = []
for _ in range(Q):
    p, x = map(int, input().split())
    queries.append([p-1, x])

counters = [0] * N
for p, x in queries:
    counters[p] += x
# print(counters)


def dfs(dist, v):
    for v_adj in tree[v]:
        if dist[v_adj] == -1:
            dist[v_adj] = 1
            counters[v_adj] += counters[v]
            dfs(dist, v_adj)


dist = [-1] * N
dist[0] = 1
# print(counters)
dfs(dist, 0)
print(*counters)
