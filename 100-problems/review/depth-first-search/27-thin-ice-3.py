#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


m_columns = int(input())
n_rows = int(input())
field = []
for _ in range(n_rows):
    col = list(map(int, input().split()))
    field.append(col)
# pprint(field)


def adj(i, j):
    up, down = [i-1, j], [i+1, j]
    left, right = [i, j-1], [i, j+1]
    adj_list = []
    for i, j in up, down, left, right:
        if 0 <= i < n_rows and 0 <= j < m_columns:
            adj_list.append([i, j])
    return adj_list


def dfs(i, j, steps):
    steps += 1
    field[i][j] = 0
    for i_adj, j_adj in adj(i, j):
        if field[i_adj][j_adj] == 0:
            continue
        dfs(i_adj, j_adj, steps)
    field[i][j] = 1
    if all(field[i_adj][j_adj] == 0 for i_adj, j_adj in adj(i, j)):
        global max_steps
        max_steps = max(max_steps, steps)


max_steps = 0
for i in range(n_rows):
    for j in range(m_columns):
        if field[i][j] == 0:
            continue
        dfs(i, j, 0)

print(max_steps)
