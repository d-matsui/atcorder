#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


w_cols, h_rows = map(int, input().split())
row_dummy = [0] * (w_cols+2)
field = [row_dummy]
for _ in range(h_rows):
    row = [0] + list(map(int, input().split())) + [0]
    field.append(row)
field.append(row_dummy)
# pprint(field)


def adj(x, y):
    east, west = [x+1, y], [x-1, y]
    if y % 2 == 1:
        south_east, north_west = [x+1, y+1], [x, y-1]
        south_west, north_east = [x, y+1], [x+1, y-1]
    else:
        south_east, north_west = [x, y+1], [x-1, y-1]
        south_west, north_east = [x-1, y+1], [x, y-1]

    adj_list = []
    for x_adj, y_adj in east, west, south_east, south_west, north_east, north_west:
        if 0 <= x_adj < w_cols+2 and 0 <= y_adj < h_rows+2:
            adj_list.append([x_adj, y_adj])
    return adj_list


def bfs(que, visited):
    count = 0
    while que:
        x, y = que.popleft()
        for x_adj, y_adj in adj(x, y):
            if visited[y_adj][x_adj] is True:
                continue
            if field[y_adj][x_adj] == 1:
                count += 1
                continue
            que.append([x_adj, y_adj])
            visited[y_adj][x_adj] = True
    return count


que = deque()
visited = [[False for x in range(w_cols + 2)] for y in range(h_rows+2)]
que.append([0, 0])
visited[0][0] = True

count = bfs(que, visited)
print(count)
