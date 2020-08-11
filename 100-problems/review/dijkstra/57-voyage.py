#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')

N, K = map(int, input().split())


def dijkstra(adj_list, s):
    que = deque()
    dist = [INF] * N

    dist[s] = 0
    que.append([s, 0])

    while que:
        u, len_s_u = que.popleft()
        if dist[u] < len_s_u:
            continue
        for v, len_u_v in adj_list[u]:
            if len_s_u + len_u_v < dist[v]:
                dist[v] = len_s_u + len_u_v
                que.append([v, dist[v]])
    return dist


# 新たに運行を開始する船舶が追加されたとき、最短経路を更新する必要があれば、
# dikstra 法を用いて最短経路を更新する
# 具体的には、
# u <-> v の重み w の辺が追加されたとき、
# w < dist[u][v] であれば、これまでより短い経路が見つかったことになるので、
# 最短経路を更新する

adj_list = [[] for _ in range(N)]
dist_all = [[INF for v in range(N)] for u in range(N)]
for _ in range(K):
    line = list(map(int, input().split()))
    if line[0] == 0:
        # order
        _, s, t = line
        # 0-index
        s -= 1
        t -= 1
        ans = -1 if dist_all[s][t] == INF else dist_all[s][t]
        print(ans)
    elif line[0] == 1:
        # new info
        _, u, v, w = line
        # 0-index
        u -= 1
        v -= 1
        adj_list[u].append([v, w])
        adj_list[v].append([u, w])
        if w < dist_all[u][v]:
            for s in range(N):
                dist_all[s] = dijkstra(adj_list, s)
