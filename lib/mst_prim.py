#!/usr/bin/env python3

from pprint import pprint

INF = float('inf')

n_nodes, m_edges = map(int, input().split())

adj_mat = [[0 for j in range(n_nodes)] for i in range(n_nodes)]
for _ in range(m_edges):
    u, v, w = map(int, input().split())
    adj_mat[u][v] = w
    adj_mat[v][u] = w
# pprint(adj_mat)


def mst_prim(n_nodes, adj_mat):
    # Prim’s Minimum Spanning Tree
    parents = [None] * n_nodes
    visited = [False] * n_nodes
    min_cost = [INF] * n_nodes

    min_cost[0] = 0
    parents[0] = -1

    while not all(visited):
        # find the vertex with minimum cost from
        # the set of vertices not yet included mst
        u = None
        cost = INF
        for v in range(n_nodes):
            if not visited[v] and min_cost[v] < cost:
                cost = min_cost[v]
                u = v
        visited[u] = True

        # update cost of the adjacent vertices of the picked vertex
        for v in range(n_nodes):
            if adj_mat[u][v] > 0 and not visited[v] and min_cost[v] > adj_mat[u][v]:
                min_cost[v] = adj_mat[u][v]
                parents[v] = u
    return parents


mst = mst_prim(n_nodes, adj_mat)
# pprint(mst)

res = 0
for child, parent in enumerate(mst):
    if parent == -1:
        continue
    res += adj_mat[parent][child]
print(res)
