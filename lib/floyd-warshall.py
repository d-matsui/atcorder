#!/usr/bin/env python3

from pprint import pprint

INF = float("inf")

n_nodes, m_edges = map(int, input().split())

edges = [[] for _ in range(n_nodes)]
for _ in range(m_edges):
    s, t, d = map(int, input().split())
    edges[s].append([t, d])
# pprint(edges)


def floyd_warshall(n_nodes, edges):
    dist = [[INF for u in range(n_nodes)] for v in range(n_nodes)]
    for u, e in enumerate(edges):
        for v, cost in e:
            dist[u][v] = cost
    for v in range(n_nodes):
        dist[v][v] = 0
    for k in range(n_nodes):
        for s in range(n_nodes):
            for t in range(n_nodes):
                dist[s][t] = min(dist[s][t], dist[s][k] + dist[k][t])
    return dist


dist = floyd_warshall(n_nodes, edges)
# pprint(dist)
