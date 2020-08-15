#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')

N, M, K = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append([u-1, v-1, w])


def unite(u, v):
    root_u = root(u)
    root_v = root(v)

    if root_u == root_v:
        return

    # assume size(root_u) >= size(root_v)
    if size(root_u) < size(root_v):
        root_u, root_v = root_v, root_u

    parents[root_u] -= size(root_v)
    parents[root_v] = root_u


def has_same_root(u, v):
    return root(u) == root(v)


def root(v):
    if parents[v] < 0:
        return v
    parents[v] = root(parents[v])
    return parents[v]


def size(v):
    return -parents[root(v)]


# Kruskal's algorithm
# 閉路を作らないようにしつつ、辺のコストが小さいものから順に選んでいく
# ある辺 e をグラフに追加したときに閉路を作るかどうかは、Union Find で判定できる
parents = [-1] * N
res = 0
count = 0
for u, v, w in sorted(edges, key=lambda e: e[2]):
    if count == N - K:
        break
    if has_same_root(u, v):
        continue
    res += w
    count += 1
    unite(u, v)

print(res)
