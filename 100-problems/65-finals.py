#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_nodes, m_edges, k_nodes = map(int, input().split())
edges = []
for _ in range(m_edges):
    u, v, w = map(int, input().split())
    edges.append([u-1, v-1, w])
# pprint(edges)


def has_same_root(u, v):
    u_root = find_root(u)
    v_root = find_root(v)
    return u_root == v_root


def find_root(v):
    if v != parents[v]:
        parents[v] = find_root(parents[v])
    return parents[v]


def unite(u, v):
    root_u = find_root(u)
    root_v = find_root(v)
    if root_u == root_v:
        return
    if size[root_u] < size[root_v]:
        root_u, root_v = root_v, root_u
    parents[root_v] = root_u
    size[root_u] += size[root_v]


edges_sorted = sorted(edges, key=lambda e: e[2])
# pprint(edges_sorted)

parents = [i for i in range(n_nodes)]
size = [1] * n_nodes

res = 0
count = 0
for u, v, w in edges_sorted:
    if count == n_nodes - k_nodes:
        break
    if not has_same_root(u, v):
        res += w
        count += 1
        unite(u, v)

print(res)
