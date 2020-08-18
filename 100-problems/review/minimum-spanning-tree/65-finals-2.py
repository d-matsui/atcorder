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
    # 0-index
    edges.append([u-1, v-1, w])

# N - K 本の辺を使うときの Minimum Spaning Tree を求めて、辺の重みの総和を求めれば良い
# Minimum Spanning Tree は Kruskal 法を使って求められる
# 閉路を作らないようにコスト最小の辺を選んでいき、Minimum Spanning Tree を求める
# ある辺をグラフに加えたときに閉路を作るかどうかは、Disjoint Set を使って判定する


def root(v):
    if parents[v] < 0:
        return v
    # update parents reccursively
    parents[v] = root(parents[v])
    return parents[v]


def has_same_root(u, v):
    return root(u) == root(v)


def size(u):
    # parent of root node has negetive value
    return - parents[root(u)]


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
    return


# 重みの昇順で辺をソート
edges = sorted(edges, key=lambda e: e[2])

parents = [-1] * N
counter = 0
total_cost = 0

for u, v, w in edges:
    if counter == N - K:
        break
    if has_same_root(u, v):
        continue
    total_cost += w
    unite(u, v)
    counter += 1

print(total_cost)
