#!/usr/bin/env python3

# 解法
# 地図の外側に余白を設け、建物が存在しない領域を塗りつぶす。
# このとき、塗りつぶした領域と建物のある領域の境界の長さの和が答えとなる。
# 境界の長さは1mなので、単に塗りつぶした領域と隣接する建物の数を求めればよい。

from pprint import pprint
from collections import deque


def init():
    col, row = map(int, input().split())

    field = []
    field.append([0 for _ in range(col + 2)])
    ex = [0]
    for _ in range(row):
        line = list(map(int, input().split()))
        line = ex + line + ex
        field.append(line)
    field.append([0 for _ in range(col + 2)])

    return row, col, field


def adj(x, y):
    w, e = [x - 1, y], [x + 1, y]
    if y % 2 == 0:
        nw, ne = [x - 1, y - 1], [x, y - 1]
        sw, se = [x - 1, y + 1], [x, y + 1]
    else:
        nw, ne = [x, y - 1], [x + 1, y - 1]
        sw, se = [x, y + 1], [x + 1, y + 1]

    return [w, e, nw, ne, sw, se]


def is_valid(x, y):
    cond_x = x >= 0 and x <= col + 1
    cond_y = y >= 0 and y <= row + 1

    return cond_x and cond_y


def fill_bsf(que, field):
    while len(que) > 0:
        x, y = que.popleft()
        for x_adj, y_adj in adj(x, y):
            if is_valid(x_adj, y_adj):
                if field[y_adj][x_adj] == 0:
                    # print(f"x_adj, y_adj: {x_adj}, {y_adj}")
                    field[y_adj][x_adj] = -1
                    que.append([x_adj, y_adj])

    return que, field


row, col, field = init()
# print(row, col)
# pprint(field)
# print(adj(2, 2))
# print(adj(3, 3))

que = deque([[0, 0]])
field[0][0] = -1
# 建物の外側領域を塗りつぶす
que, field = fill_bsf(que, field)
# pprint(field)

res = 0
for x in range(1, col + 1):
    for y in range(1, row + 1):
        if field[y][x] == 1:
            # 建物に隣接する塗り潰し領域の数を求める
            for x_adj, y_adj in adj(x, y):
                if field[y_adj][x_adj] == -1:
                    res += 1

print(res)
