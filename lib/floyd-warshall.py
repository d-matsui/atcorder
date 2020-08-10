#!/usr/bin/env python3

from pprint import pprint

INF = float("inf")

n_nodes, m_edges = map(int, input().split())

adj_list = [[] for _ in range(n_nodes)]
for _ in range(m_adj_list):
    u, v, w = map(int, input().split())
    adj_list[u].append([v, w])
    adj_list[v].append([u, w])


def floyd_warshall(n_nodes, adj_list):
    dist = [[0 if u == v else INF for v in range(N)] for u in range(N)]
    for v in range(N):
        for u, w in adj_list[v]:
            dist[u][v] = w

    for k in range(n_nodes):
        for s in range(n_nodes):
            for t in range(n_nodes):
                dist[s][t] = min(dist[s][t], dist[s][k] + dist[k][t])
    return dist


dist = floyd_warshall(n_nodes, adj_list)
# pprint(dist)
