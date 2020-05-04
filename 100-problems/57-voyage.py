#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

n_nodes, k_inputs = map(int, input().split())
inputs = []
for _ in range(k_inputs):
    line = list(map(int, input().split()))
    inputs.append(line)
# pprint(inputs)


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


edges = [[] for _ in range(n_nodes)]
dist = [[INF for u in range(n_nodes)] for v in range(n_nodes)]
for v in range(n_nodes):
    dist[v][v] = 0

res = []
for line in inputs:
    if line[0] == 0:
        # order
        _, start, goal = line
        start -= 1
        goal -= 1
        if dist[start][goal] == INF:
            res.append(-1)
        else:
            res.append(dist[start][goal])
    else:
        # info
        _, u, v, cost = line
        u -= 1
        v -= 1
        edges[u].append([v, cost])
        edges[v].append([u, cost])
        if cost < dist[u][v]:
            for v in range(n_nodes):
                dist[v] = dijkstra(n_nodes, edges, v)

for r in res:
    print(r)
