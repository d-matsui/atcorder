#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


m_rows, n_cols = map(int, input().split())
k_regions = int(input())
field = []
for _ in range(m_rows):
    col = list(input())
    field.append(col)
region_list = []
for _ in range(k_regions):
    a, b, c, d = map(int, input().split())
    region_list.append([a-1, b-1, c-1, d-1])
# pprint(field)
# pprint(region_list)

# s[i][j][x] := [0, i), [0, j) の長方形区間にある x の数
# s[i+1][j+1][x] = s[i][j+1] + s[i+1][j] - s[i][j] + a[i][j]

# [a, c+1), [b, d+1)  の長方形区間にある x の数は以下で与えられる
# s[c+1][d+1][x] - s[c+1][b][x] - s[a][d+1][x] + s[a][b]
# d = {J: 0, O: 1, I: 2}

s = [[[0 for x in range(3)] for j in range(n_cols+1)] for i in range(m_rows+1)]
d = {'J': 0, 'O': 1, 'I': 2}

for i in range(m_rows):
    for j in range(n_cols):
        for x in range(3):
            s[i+1][j+1][x] = s[i][j+1][x] + s[i+1][j][x] - s[i][j][x]
        x = d[field[i][j]]
        s[i+1][j+1][x] += 1
# pprint(s)

for a, b, c, d in region_list:
    ans_list = []
    for x in range(3):
        ans = s[c+1][d+1][x] - s[c+1][b][x] - s[a][d+1][x] + s[a][b][x]
        ans_list.append(ans)
    print(*ans_list)
