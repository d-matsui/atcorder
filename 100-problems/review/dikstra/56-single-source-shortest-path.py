#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import heapq
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M, r = map(int, input().split())

adj_list = [[] for _ in range(N)]

for _ in range(M):
    s, t, d = map(int, input().split())
    adj_list[s].append([t, d])
# print(adj_list)


# def dikstra(adj_list, source):
#     que = deque()
#     dist = [INF] * N

#     dist[source] = 0
#     que.append([source, 0])

#     while que:
#         u, len_s_u  = que.popleft()
#         if dist[u] < len_s_u:
#             continue
#         for v, len_u_v in adj_list[u]:
#             if len_s_u + len_u_v < dist[v]:
#                 dist[v] = len_s_u + len_u_v
#                 que.append([v, dist[v]])
#     return dist


def dikstra(adj_list, source):
    visited = defaultdict()
    dist = [INF] * N
    prev = [None] * N
    que = []

    visited[source] = True
    dist[source] = 0
    heapq.heappush(que, (dist[source], source))

    while que:
        len_s_u, u = heapq.heappop(que)
        if visited[u]:
            continue
        visited[u] = True
        for v, len_u_v in adj_list[u]:
            if len_s_u + len_u_v < dist[v]:
                dist[v] = len_s_u + len_u_v
                prev[v] = u
                heapq.heappush(que, (dist[v], v))
    return dist, prev


dist, prev = dikstra(adj_list, r)
for d in dist:
    if d == INF:
        print('INF')
    else:
        print(d)
