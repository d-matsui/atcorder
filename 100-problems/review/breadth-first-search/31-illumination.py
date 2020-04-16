#!/usr/bin/env python3

from pprint import pprint
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

w_col, h_row = map(int, input().split())

row_dummy = [0 for _ in range(w_col + 2)]
field = []
field.append(row_dummy)
for i in range(h_row):
    line = list(map(int, input().split()))
    field.append([0] + line + [0])
field.append(row_dummy)
# pprint(field)


def adj(x, y):
    left, right = [x - 1, y], [x + 1, y]
    if y % 2 == 1:
        up_left, up_right = [x, y - 1], [x + 1, y - 1]
        down_left, down_right = [x, y + 1], [x + 1, y + 1]
    else:
        up_left, up_right = [x - 1, y - 1], [x, y - 1]
        down_left, down_right = [x - 1, y + 1], [x, y + 1]
    res = []
    for x_next, y_next in left, right, up_left, up_right, down_left, down_right:
        if 0 <= x_next < w_col + 2 and 0 <= y_next < h_row + 2:
            res.append([x_next, y_next])
    return res


def bfs(que, dist, count):
    while len(que) > 0:
        x, y = que.popleft()
        for x_next, y_next in adj(x, y):
            if field[y_next][x_next] == 1:
                count += 1
            else:
                if dist[y_next][x_next] == -1:
                    dist[y_next][x_next] = dist[y_next][x_next] + 1
                    que.append([x_next, y_next])
    return dist, count


que = deque()
dist = [[-1 for j in range(w_col + 2)] for i in range(h_row + 2)]

que.append([0, 0])
dist[0][0] = 0
count = 0
dist, count = bfs(que, dist, count)

print(count)
