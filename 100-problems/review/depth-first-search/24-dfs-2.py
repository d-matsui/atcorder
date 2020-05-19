#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_nodes = int(input())
graph = [[] for _ in range(n_nodes)]

for _ in range(n_nodes):
    line = list(map(int, input().split()))
    u, k = line[0], line[1]
    if k > 0:
        for v in line[2:]:
            graph[u - 1].append(v - 1)
# pprint(graph)


def dfs(v):
    global time
    time += 1
    for v_adj in graph[v]:
        if d[v_adj] == -1:
            d[v_adj] = time
            dfs(v_adj)
    f[v] = time
    time += 1


d = [-1] * n_nodes
f = [-1] * n_nodes
time = 1

for v in range(n_nodes):
    if d[v] == -1:
        d[v] = time
        dfs(v)

# pprint(d)
# pprint(f)

for v in range(n_nodes):
    print(f"{v + 1} {d[v]} {f[v]}")
