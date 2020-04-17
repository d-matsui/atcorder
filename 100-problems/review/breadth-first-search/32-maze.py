#!/usr/bin/env python3

from pprint import pprint
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    res = []
    for i_next, j_next in up, down, left, right:
        if 0 <= i_next < height and 0 <= j_next < width:
            if [i_next, j_next] == left:
                if walls[i * 2][j - 1] == 0:
                    res.append([i_next, j_next])
            elif [i_next, j_next] == right:
                if walls[i * 2][j] == 0:
                    res.append([i_next, j_next])
            elif [i_next, j_next] == up:
                if walls[2 * i - 1][j] == 0:
                    res.append([i_next, j_next])
            else:
                if walls[2 * i + 1][j] == 0:
                    res.append([i_next, j_next])
    return res


def bfs(que, dist):
    while len(que) > 0:
        i, j = que.popleft()
        for i_next, j_next in adj(i, j):
            if dist[i_next][j_next] == -1:
                dist[i_next][j_next] = dist[i][j] + 1
                que.append([i_next, j_next])
    return dist


while True:
    width, height = map(int, input().split())
    if width == 0 and height == 0:
        break
    walls = []
    for _ in range(2 * height - 1):
        line = list(map(int, input().split()))
        walls.append(line)
    # pprint(walls)

    maze = [[-1 for j in range(width)] for i in range(height)]
    que = deque()
    dist = [[-1 for j in range(width)] for i in range(height)]

    start = [0, 0]
    que.append(start)
    dist[0][0] = 0

    dist = bfs(que, dist)
    print(dist[height - 1][width - 1] + 1)
