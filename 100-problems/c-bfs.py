#!/usr/bin/env python3

from collections import deque

row, column = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = []
for i in range(row):
    line = list(input())
    maze.append(line)
# print(maze)


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    return [up, down, left, right]


edges = [[] for _ in range(row * column)]
for i in range(1, row - 1):
    for j in range(1, column - 1):
        # print(f"\ni, j: {i}, {j}")
        for i_adj, j_adj in adj(i, j):
            if maze[i][j] == '.' and maze[i_adj][j_adj] == '.':
                # print(f"i_adj, j_adj: {i_adj}, {j_adj}")
                u = i * column + j
                v = i_adj * column + j_adj
                # print(f"{u}->{v}")
                edges[u].append(v)
# print(edges)


def bfs(que, dist):
    while len(que) > 0:
        v = que.popleft()
        for v_adj in edges[v]:
            if dist[v_adj] == -1:
                dist[v_adj] = dist[v] + 1
                que.append(v_adj)


que = deque()
dist = [-1 for _ in range(row * column)]
v = (sy - 1) * column + sx - 1
dist[v] = 0
que.append(v)
bfs(que, dist)

v = (gy - 1) * column + gx - 1
print(dist[v])
