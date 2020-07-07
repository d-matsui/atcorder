#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


h_rows, w_cols, n_cheeses = map(int, input().split())
field = []
for _ in range(h_rows):
    col = list(input())
    field.append(col)
# pprint(field)

pos_start = [-1, -1]
list_pos_goal = {}
for i in range(h_rows):
    for j in range(w_cols):
        if field[i][j] == '.' or field[i][j] == 'X':
            continue
        if field[i][j] == 'S':
            pos_start[0] = i
            pos_start[1] = j
        else:
            list_pos_goal[int(field[i][j])] = [i, j]
# print(pos_start, list_pos_goal)


def adj(i, j):
    up, down = [i-1, j], [i+1, j]
    left, right = [i, j-1], [i, j+1]
    adj_list = []
    for i_adj, j_adj in up, down, left, right:
        if 0 <= i_adj < h_rows and 0 <= j_adj < w_cols:
            if field[i_adj][j_adj] == 'X':
                continue
            adj_list.append([i_adj, j_adj])
    return adj_list


def bfs(que, dist, pos_goal):
    # print(f'pos_goal = {pos_goal}')
    while que:
        i, j = que.popleft()
        # print(f'i, j = {i, j}')
        if [i, j] == pos_goal:
            return dist[i][j]
        for i_adj, j_adj in adj(i, j):
            if dist[i_adj][j_adj] == -1:
                que.append([i_adj, j_adj])
                dist[i_adj][j_adj] = dist[i][j] + 1

time = 0
for goal in range(1, n_cheeses + 1):
    dist = [[-1 for j in range(w_cols)] for i in range(h_rows)]
    que = deque()
    # print(f'goal = {goal}')
    if goal > 1:
        pos_start = list_pos_goal[goal-1]
    dist[pos_start[0]][pos_start[1]] = 0
    que.append(pos_start)
    pos_goal = list_pos_goal[goal]
    time += bfs(que, dist, pos_goal)
    # print(f'time = {time}')
print(time)
