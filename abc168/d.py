#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_nodes, m_edges = map(int, input().split())
edges = [[] for _ in range(n_nodes)]
for _ in range(m_edges):
    u, v = map(int, input().split())
    edges[u - 1].append([v - 1, 1])
    edges[v - 1].append([u - 1, 1])
# pprint(edges)

parents = [-1] * n_nodes


def dijkstra(n_nodes, edges, start):
    que = deque()
    dist = [INF] * n_nodes
    dist[start] = 0
    que.append([start, 0])
    while len(que) > 0:
        v, v_cost = que.popleft()
        if dist[v] < v_cost:
            continue
        for u, u_cost in edges[v]:
            if v_cost + u_cost < dist[u]:
                dist[u] = v_cost + u_cost
                parents[u] = v
                que.append([u, dist[u]])
    return dist


start = 0
dist = dijkstra(n_nodes, edges, start)
# print(dist)
# print(parents)

print('Yes')
for i in range(1, n_nodes):
    print(parents[i] + 1)
