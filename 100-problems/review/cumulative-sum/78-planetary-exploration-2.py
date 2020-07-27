#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


M, N = map(int, input().split())
K = int(input())
field = []
for _ in range(M):
    line = list(input())
    field.append(line)
pprint(field)

regions = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    # 0-index
    regions.append([a-1, b-1, c-1, d-1])

# J, O, I = 0, 1, 2
# s[i][j][k] := (0, 0) ~ (i-1, j-1) の領域にある k の数
# s[i+1][j+1][k] = s[i+1][j][k] + s[i][j+1][k] - s[i][j][k] + A[i][j][k]

s = [[[0 for k in range(3)] for j in range(N+1)] for i in range(M+1)]
d = {'J': 0, 'O': 1, 'I': 2}

for i in range(M):
    for j in range(N):
        k = d[field[i][j]]
        s[i+1][j+1][k] = 1
        for k in range(3):
            s[i+1][j+1][k] += s[i+1][j][k] + s[i][j+1][k] - s[i][j][k]

# (a, b) ~ (c, d) の領域にある k の数
# s[c+1][d+1][k] - s[a][d+1][k] - s[c+1][b][k] + s[a][b][k]

for a, b, c, d in regions:
    ans_list = []
    for k in range(3):
        ans = s[c+1][d+1][k] - s[a][d+1][k] - s[c+1][b][k] + s[a][b][k]
        ans_list.append(ans)
    print(*ans_list)
