#!/usr/bin/env python3

from pprint import pprint
from collections import deque


def init(w, h):
    walls = []
    for _ in range(2 * h - 1):
        line = list(map(int, input().split()))
        walls.append(line)

    keys = [(x, y) for x in range(w) for y in range(h)]
    values = [-1 for _ in range(w * h)]
    dist = dict(zip(keys, values))

    que = deque()

    return walls, dist, que


def is_valid(x, y):
    cond_x = x >= 0 and x < w
    cond_y = y >= 0 and y < h
    return cond_x and cond_y


def is_reachable(x, y, move):
    if move == 'up':
        if walls[2 * y - 1][x] == 1:
            return False
    elif move == 'down':
        if walls[2 * y + 1][x] == 1:
            return False
    elif move == 'left':
        if walls[2 * y][x - 1] == 1:
            return False
    else:
        # move == right
        if walls[2 * y][x] == 1:
            return False
    return True


def adj(x, y):
    up, down = [x, y - 1, 'up'], [x, y + 1, 'down']
    left, right = [x - 1, y, 'left'], [x + 1, y, 'right']
    res = []
    for x_adj, y_adj, move in [up, down, left, right]:
        # print(f"x_adj, y_adj: {x_adj}, {y_adj}")
        if is_valid(x_adj, y_adj) and is_reachable(x, y, move):
            res.append([x_adj, y_adj])
    return res


def bfs(dist, que):
    while len(que) > 0:
        x, y = que.popleft()
        for x_adj, y_adj in adj(x, y):
            if dist[(x_adj, y_adj)] == -1:
                dist[(x_adj, y_adj)] = dist[(x, y)] + 1
                que.append((x_adj, y_adj))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    walls, dist, que = init(w, h)

    que.append((0, 0))
    dist[(0, 0)] = 0
    bfs(dist, que)

    if dist[(w - 1, h - 1)] == -1:
        print(0)
    else:
        print(dist[(w - 1, h - 1)] + 1)
