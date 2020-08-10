#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u-1].append([v-1, w])
    adj_list[v-1].append([u-1, w])


def floyd_warshall(n_nodes, adj_list):
    distances = [[0 if u == v else INF for v in range(N)] for u in range(N)]
    for v in range(N):
        for u, w in adj_list[v]:
            distances[u][v] = w

    for k in range(N):
        for s in range(N):
            for t in range(N):
                distances[s][t] = min(distances[s][t], distances[s][k] + distances[k][t])

    return distances


distances = floyd_warshall(N, adj_list)

ans = min(map(max, distances))
print(ans)
