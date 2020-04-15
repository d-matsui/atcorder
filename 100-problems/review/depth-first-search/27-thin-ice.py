#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

m_col = int(input())
n_row = int(input())

field = []
for _ in range(n_row):
    line = list(map(int, input().split()))
    field.append(line)

# print(m_col, n_row)
# print(field)


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    res = []
    for i_next, j_next in up, down, left, right:
        if 0 <= i_next < n_row and 0 <= j_next < m_col:
            res.append([i_next, j_next])
    return res


def dfs(i, j, steps, field):
    steps += 1
    field[i][j] = 0
    for i_next, j_next in adj(i, j):
        if field[i_next][j_next] == 1:
            dfs(i_next, j_next, steps, field)
    field[i][j] = 1
    if all(field[i_next][j_next] == 0 for i_next, j_next in adj(i, j)):
        global max_steps
        max_steps = max(max_steps, steps)


max_steps = 0
for i in range(n_row):
    for j in range(m_col):
        if field[i][j] == 1:
            dfs(i, j, 0, field)

print(max_steps)
