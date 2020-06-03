#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = 10 ** 10

n_nodes, m_edges = map(int, input().split())
dist = [[INF] * n_nodes for _ in range(n_nodes)]

for _ in range(m_edges):
    s, t, d = map(int, input().split())
    dist[s][t] = d

memory = {}
end = 2 ** n_nodes - 1


def rec(state, pos):
    if (state, pos) in memory:
        return memory[(state, pos)]

    if state == end:
        return dist[pos][0]

    mask = 1
    res = INF
    for pos_next in range(n_nodes):
        if mask & state:
            mask <<= 1
            continue

        res = min(res, rec(state | mask, pos_next) + dist[pos][pos_next])
        mask <<= 1

    memory[(state, pos)] = res
    return res


res = rec(1, 0)
if res == INF:
    print(-1)
else:
    print(res)
