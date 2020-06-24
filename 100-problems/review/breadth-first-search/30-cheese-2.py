#!/usr/bin/env python3

from pprint import pprint
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


h_rows, w_cols, n_cheese = map(int, input().split())
field = []
for _ in range(h_rows):
    col = list(input())
    field.append(col)
# pprint(field)


def adj(i, j):
    up, down = [i-1, j], [i+1, j]
    left, right = [i, j-1], [i, j+1]

    adj_list = []
    for i_adj, j_adj in up, down, left, right:
        if 0 <= i_adj <= h_rows - 1 and 0 <= j_adj <= w_cols - 1:
            if field[i_adj][j_adj] == 'X':
                continue
            adj_list.append([i_adj, j_adj])

    return adj_list


def bfs(que, dist):
    while len(que) > 0:
        i, j = que.popleft()
        for i_adj, j_adj in adj(i, j):
            if dist[i_adj][j_adj] == -1:
                dist[i_adj][j_adj] = dist[i][j] + 1
                que.append((i_adj, j_adj))
    return dist


pos_factory = {}
for i in range(h_rows):
    for j in range(w_cols):
        if field[i][j] != '.' and field[i][j] != 'X':
            key = field[i][j]
            pos_factory[key] = (i, j)

total = 0
que = deque()
for start in range(n_cheese):
    dist = [[-1 for j in range(w_cols)] for i in range(h_rows)]
    if start == 0:
        pos_start = pos_factory['S']
        pos_goal = pos_factory['1']
    else:
        pos_start = pos_factory[str(start)]
        pos_goal = pos_factory[str(start + 1)]

    dist[pos_start[0]][pos_start[1]] = 0
    que.append(pos_start)
    dist = bfs(que, dist)
    total += dist[pos_goal[0]][pos_goal[1]]

print(total)
