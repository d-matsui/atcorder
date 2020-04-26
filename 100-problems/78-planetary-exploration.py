#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
inf = float("inf")

m_rows, n_cols = map(int, input().split())
k_regions = int(input())

field = []
for _ in range(m_rows):
    line = list(input())
    field.append(line)

regions = []
for _ in range(k_regions):
    a, b, c, d = map(int, input().split())
    regions.append([a - 1, b - 1, c - 1, d - 1])

pprint(field)
pprint(regions)

# s[i + 1][j + 1][x] := (0, 0)から(i, j)の領域にあるxの数
# x = {0, 1, 2}, 0: Jungle, 1: Ocean, 2: Ice
cum_sum = [[[0 for x in range(3)] for j in range(n_cols + 1)] for i in range(m_rows + 1)]

for i in range(m_rows):
    for j in range(n_cols):
        if field[i][j] == 'J':
            x = 0
        elif field[i][j] == 'O':
            x = 1
        else:
            x = 2
        print(f"i = {i}, j = {j}, x = {x}")
        cum_sum[i + 1][j + 1][x] = cum_sum[i][j + 1][x] + cum_sum[i + 1][j][x] - cum_sum[i][j][x] + 1

pprint(cum_sum[1][2])
