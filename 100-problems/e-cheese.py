#!/usr/bin/env python3

from collections import deque

row, col, n = map(int, input().split())

field = []
for _ in range(row):
    line = list(input())
    field.append(line)
# print(row, col, n)
# print(field)


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]

    if i == 0:
        if j == 0:
            return [down, right]
        elif j == col - 1:
            return [down, left]
        else:
            return [down, left, right]
    elif i == row - 1:
        if j == 0:
            return [up, right]
        elif j == col - 1:
            return [up, left]
        else:
            return [up, left, right]
    else:
        if j == 0:
            return [up, down, right]
        elif j == col - 1:
            return [up, down, left]
        else:
            return [up, down, left, right]


edges = [[] for _ in range(row * col)]
for i in range(0, row):
    for j in range(0, col):
        for i_adj, j_adj in adj(i, j):
            if field[i][j] != 'X' and field[i_adj][j_adj] != 'X':
                u = i * col + j
                v = i_adj * col + j_adj
                edges[u].append(v)
# print(edges)

pos_list = {}
for i in range(row):
    for j in range(col):
        if field[i][j] != '.' or field[i][j] != 'X':
            if field[i][j] == 'S':
                pos_list[0] = [i, j]
            else:
                for k in range(1, n + 1):
                    if field[i][j] == str(k):
                        pos_list[k] = [i, j]
# print(pos_list)


def bfs(que, dist):
    while len(que) > 0:
        v = que.popleft()
        for v_next in edges[v]:
            if dist[v_next] == -1:
                dist[v_next] = dist[v] + 1
                que.append(v_next)


total = 0
for goal in range(1, n + 1):
    dist = [-1 for _ in range(row * col)]
    que = deque()

    if goal == 1:
        v_start = pos_list[0][0] * col + pos_list[0][1]
    else:
        v_start = pos_list[goal - 1][0] * col + pos_list[goal - 1][1]
    dist[v_start] = 0
    que.append(v_start)

    bfs(que, dist)
    v_goal = pos_list[goal][0] * col + pos_list[goal][1]
    total += dist[v_goal]

print(total)
