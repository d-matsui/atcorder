#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n_nodes, q_query = map(int, input().split())

edges = [[] for _ in range(n_nodes)]
for _ in range(n_nodes - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

queries = []
for _ in range(q_query):
    p, x = map(int, input().split())
    queries.append([p - 1, x])

# print(n_nodes, q_query)
# print(edges, queries)

res = [0 for _ in range(n_nodes)]
for node, point in queries:
    res[node] += point


def dfs(v, parent):
    for v_next in edges[v]:
        if v_next != parent:
            res[v_next] += res[v]
            dfs(v_next, v)


dfs(0, None)

print(*res)
