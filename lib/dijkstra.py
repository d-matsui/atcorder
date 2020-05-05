#!/usr/bin/env python3
from collections import deque
INF = float("inf")

n_nodes, m_edges, start = map(int, input().split())

edges = [[] for _ in range(n_nodes)]
for _ in range(m_edges):
    s, t, d = map(int, input().split())
    edges[s].append([t, d])


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
