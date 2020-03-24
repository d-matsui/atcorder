#!/usr/bin/env python3

import sys

input = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

query = []
for _ in range(Q):
    p, x = map(int, input().split())
    query.append([p, x])

counter = [0 for _ in range(N)]
for p, x in query:
    counter[p - 1] += x


def dfs(v, parent):
    for v_next in edges[v]:
        if v_next != parent:
            counter[v_next] += counter[v]
            dfs(v_next, v)


root = 0
dfs(root, None)

print(*counter)
