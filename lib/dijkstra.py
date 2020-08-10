#!/usr/bin/env python3
import heapq
INF = float("inf")

n_nodes, m_edges, start = map(int, input().split())

adj_list = [[] for _ in range(n_nodes)]
for _ in range(m_edges):
    s, t, d = map(int, input().split())
    adj_list[s].append([t, d])


def dijkstra(n_nodes, adj_list, start):
    distances = {vertex: INF for vertex in range(n_nodes)}
    distances[start] = 0
    pq = [[distances[start], start]]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                heapq.heappush(pq, [distance, neighbor])
    return distances


distances = dijkstra(n_nodes, adj_list, start)

for v in range(n_nodes):
    if distances[v] == INF:
        print('INF')
    else:
        print(distances[v])
