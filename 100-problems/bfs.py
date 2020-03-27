#!/usr/bin/env python3

from collections import deque

n = int(input())

edges = [[] for _ in range(n)]
for _ in range(n):
    line = list(map(int, input().split()))
    u = line[0] - 1
    if len(line) != 2:
        v_list = line[1:]
        for v in v_list:
            edges[u].append(v - 1)
# print(n, edges)

dist = [-1 for _ in range(n)]
que = deque()


def dfs(que, dist):
    while len(que) > 0:
        v = que.popleft()

        for v_adj in edges[v]:
            if dist[v_adj] == -1:
                dist[v_adj] = dist[v] + 1
                que.append(v_adj)


dist[0] = 0
que.appendleft(0)
dfs(que, dist)

for i in range(n):
    print(f"{i + 1} {dist[i]}")
