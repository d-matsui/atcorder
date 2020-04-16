#!/usr/bin/env python3

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

h_row, w_col, n_cheese = map(int, input().split())
# print(h_row, w_col, n_cheese)

field = []
for _ in range(h_row):
    line = list(input())
    field.append(line)
# print(field)


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    res = []
    for i_next, j_next in up, down, left, right:
        if 0 <= i_next < h_row and 0 <= j_next < w_col:
            if field[i_next][j_next] != 'X':
                res.append([i_next, j_next])
    return res


def bfs(que, dist):
    while len(que) > 0:
        # print(f"que = {que}")
        i, j = que.popleft()
        # print(f"i, j = {i}, {j}")
        for i_next, j_next in adj(i, j):
            if dist[i_next][j_next] == -1:
                # print(f"i_next, j_next = {i_next}, {j_next}")
                dist[i_next][j_next] = dist[i][j] + 1
                que.append((i_next, j_next))
                # print(f"que_next = {que}")
    return dist


pos_factories = {}
for i in range(h_row):
    for j in range(w_col):
        if field[i][j] != '.' or field[i][j] != 'X':
            key = field[i][j]
            pos_factories[key] = (i, j)

total = 0
que = deque()
for start in range(n_cheese):
    dist = [[-1 for j in range(w_col)] for i in range(h_row)]
    if start == 0:
        pos_start = pos_factories['S']
        pos_goal = pos_factories['1']
    else:
        pos_start = pos_factories[str(start)]
        pos_goal = pos_factories[str(start + 1)]
    dist[pos_start[0]][pos_start[1]] = 0
    que.append(pos_start)
    dist = bfs(que, dist)
    total += dist[pos_goal[0]][pos_goal[1]]

print(total)
