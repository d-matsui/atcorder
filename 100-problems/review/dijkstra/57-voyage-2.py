#!/usr/bin/env python3

from pprint import pprint
import heapq
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, K = map(int, input().split())
adj_list = [[] for v in range(N)]


def dijkstra(adj_list, n_nodes, source):
    distances = [0 if v == source else INF for v in range(n_nodes)]
    priority_queue = [[distances[source], source]]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        if current_distance > distances[current]:
            continue
        for neighbor, weight in adj_list[current]:
            if current_distance + weight < distances[neighbor]:
                distances[neighbor] = current_distance + weight
                heapq.heappush(priority_queue, [distances[neighbor], neighbor])

    return distances


distances_all = [[0 if u == v else INF for v in range(N)] for u in range(N)]
for _ in range(K):
    line = list(map(int, input().split()))
    if line[0] == 0:
        # order
        _, source, dest = line
        source -= 1
        dest -= 1
        if distances_all[source][dest] == INF:
            print(-1)
        else:
            print(distances_all[source][dest])
    else:
        # information
        _, source, dest, weight = line
        source -= 1
        dest -= 1
        adj_list[source].append([dest, weight])
        adj_list[dest].append([source, weight])
        if distances_all[source][dest] > weight:
            for source in range(N):
                distances_all[source] = dijkstra(adj_list, N, source)
