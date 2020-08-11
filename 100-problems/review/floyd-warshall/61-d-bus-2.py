#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M = map(int, input().split())
adj_list = [[] for v in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u-1].append([v-1, w])
    adj_list[v-1].append([u-1, w])
# pprint(adj_list)


def floyd_warshall(adj_list, N):
    distances = [[0 if u == v else INF for v in range(N)] for u in range(N)]
    for u in range(N):
        for v, w in adj_list[u]:
            distances[u][v] = w

    for k in range(N):
        for u in range(N):
            for v in range(N):
                distance = distances[u][k] + distances[k][v]
                if distance < distances[u][v]:
                    distances[u][v] = distance

    return distances


distances = floyd_warshall(adj_list, N)
ans = min([max(distances[u]) for u in range(N)])
print(ans)
