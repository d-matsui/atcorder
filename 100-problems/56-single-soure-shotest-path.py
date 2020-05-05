#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

n_nodes, m_edges, start = map(int, input().split())

edges = [[] for _ in range(n_nodes)]
for _ in range(m_edges):
    s, t, d = map(int, input().split())
    edges[s].append([t, d])
# print(edges)


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
                que.append([u, dist[u]])
    return dist


dist = dijkstra(n_nodes, edges, start)
# pprint(dist)

for d in dist:
    if d == INF:
        print('INF')
    else:
        print(d)
