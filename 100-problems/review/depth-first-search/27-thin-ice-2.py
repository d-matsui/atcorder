#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


m_cols = int(input())
n_rows = int(input())
field = []
for _ in range(n_rows):
    col = list(map(int, input().split()))
    field.append(col)
# pprint(field)


def adj(i, j):
    top, bottom = [i-1, j], [i+1, j]
    left, right = [i, j-1], [i, j+1]

    adj_list = []
    for i_adj, j_adj in top, bottom, left, right:
        if 0 <= i_adj <= n_rows - 1 and 0 <= j_adj <= m_cols - 1:
            adj_list.append([i_adj, j_adj])

    return adj_list


def dfs(i, j, steps, field):
    steps += 1
    field[i][j] = 0
    for i_adj, j_adj in adj(i, j):
        if field[i_adj][j_adj] == 0:
            continue
        dfs(i_adj, j_adj, steps, field)
    field[i][j] = 1
    if all(field[i_adj][j_adj] == 0 for i_adj, j_adj in adj(i, j)):
        global max_steps
        max_steps = max(max_steps, steps)


max_steps = 0
for i in range(n_rows):
    for j in range(m_cols):
        if field[i][j] == 0:
            continue
        dfs(i, j, 0, field)

print(max_steps)
