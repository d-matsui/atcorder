#!/usr/bin/env python3

from pprint import pprint
import heapq
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M, source = map(int, input().split())
adj_list = [[] for v in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append([v, w])
# pprint(adj_list)


def dijkstra(n_nodes, adj_list, source):
    dist = [0 if v == source else INF for v in range(n_nodes)]
    priority_queue = [[dist[source], source]]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        if current_distance > dist[current]:
            continue
        for neighbor, distance in adj_list[current]:
            if current_distance + distance < dist[neighbor]:
                dist[neighbor] = current_distance + distance
                heapq.heappush(priority_queue, [dist[neighbor], neighbor])

    return dist


dist = dijkstra(N, adj_list, source)

for v in range(N):
    if dist[v] == INF:
        print('INF')
    else:
        print(dist[v])
