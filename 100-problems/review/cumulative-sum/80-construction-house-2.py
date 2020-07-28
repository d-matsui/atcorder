#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


H, W, K, V = map(int, input().split())
A = []
for _ in range(H):
    line = list(map(int, input().split()))
    A.append(line)

# s[i][j] = (0, 0) ~ (i-1, j-1) の領域の地価の総和
# 0 <= i <= H, 0 <= j <= W
# s[0][0] = 0
# s[i][j] = s[i][j-1] + s[i-1][j] + A[i-1][j-1] - s[i-1][j-1]

s = [[0 for j in range(W+1)] for i in range(H+1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        s[i][j] += A[i-1][j-1]

for i in range(1, H+1):
    for j in range(1, W+1):
        s[i][j] += s[i][j-1] + s[i-1][j] - s[i-1][j-1]

# (i_1, j_1) ~ (i_2, j_2) の領域の地価の総和
# s[i_2-1][j_2-1] - s[i_1][j_2] - s[i_2][j_1] + s[i_1][j_1]

def can_construct(i_1, j_1, i_2, j_2, V, K):
    # print(i_1, j_1, i_2, j_2)
    cost_buy = s[i_2][j_2] - s[i_1][j_2] - s[i_2][j_1] + s[i_1][j_1]
    cost_build = (i_2 - i_1) * (j_2 - j_1) * K
    if cost_buy + cost_build <= V:
        return True
    return False

max_area = 0
for i_1 in range(H):
    for j_1 in range(W):
        for i_2 in range(i_1+1, H+1):
            for j_2 in range(j_1+1, W+1):
                if not can_construct(i_1, j_1, i_2, j_2, V, K):
                    continue
                max_area = max(max_area, (i_2 - i_1) * (j_2 - j_1))

print(max_area)
