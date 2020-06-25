#!/usr/bin/env python3

from pprint import pprint
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


W, H = map(int, input().split())
dummy_row = [0] * (W + 2)
field = [dummy_row]
for _ in range(H):
    dummy = [0]
    row = dummy + list(map(int, input().split())) + dummy
    field.append(row)
field.append(dummy_row)
# pprint(field)

def adj(x, y):
    left, right = [x-1, y], [x+1, y]
    if y % 2 == 1:
        up_left, up_right = [x, y-1], [x+1, y-1]
        down_left, down_right = [x, y+1], [x+1, y+1]
    else:
        up_left, up_right = [x-1, y-1], [x, y-1]
        down_left, down_right = [x-1, y+1], [x, y+1]

    adj_list = []
    for x_adj, y_adj in left, right, up_left, up_right, down_left, down_right:
        if 0 <= x_adj < W + 2 and 0 <= y_adj < H + 2:
            adj_list.append([x_adj, y_adj])
    return adj_list


def bfs(que, visited, count):
    while len(que) > 0:
        x, y = que.popleft()
        for x_adj, y_adj in adj(x, y):
            i_adj, j_adj = y_adj, x_adj
            if field[i_adj][j_adj] == 1:
                count += 1
            else:
                if visited[i_adj][j_adj] is True:
                    continue
                visited[i_adj][j_adj] = True
                que.append([x_adj, y_adj])
    return count


que = deque()
visited = [[False for j in range(W + 2)] for i in range(H + 2)]
que.append([0, 0])
visited[0][0] = True
count = 0
count = bfs(que, visited, count)

print(count)
