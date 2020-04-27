#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

m_rows, n_cols = map(int, input().split())
k_regions = int(input())

field = []
for _ in range(m_rows):
    line = list(input().decode().rstrip())
    field.append(line)

regions = []
for _ in range(k_regions):
    a, b, c, d = map(int, input().split())
    regions.append([a - 1, b - 1, c - 1, d - 1])

# pprint(field)
# pprint(regions)

# s[i][j][x] := [0, x) \times [0, y) の長方形区間にあるxの数
# s[i+1][j+1][x] = s[i][j+1] + s[i+1][j] - s[i][j] + a[i][j]
# x = {0, 1, 2}, 0: Jungle, 1: Ocean, 2: Ice
cum_sum = [[[0 for x in range(3)] for j in range(n_cols + 1)] for i in range(m_rows + 1)]

for i in range(m_rows):
    for j in range(n_cols):
        for x in range(3):
            cum_sum[i+1][j+1][x] = cum_sum[i][j+1][x] + cum_sum[i+1][j][x] - cum_sum[i][j][x]
        if field[i][j] == 'J':
            x = 0
        elif field[i][j] == 'O':
            x = 1
        else:
            x = 2
        cum_sum[i+1][j+1][x] += 1
# pprint(cum_sum)

for i_1, j_1, i_2, j_2 in regions:
    res = []
    for x in range(3):
        r = cum_sum[i_2+1][j_2+1][x] - cum_sum[i_2+1][j_1][x] - cum_sum[i_1][j_2+1][x] + cum_sum[i_1][j_1][x]
        res.append(r)
    print(*res)
