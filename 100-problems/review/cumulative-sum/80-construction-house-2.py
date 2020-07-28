#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


H, W, K, V = map(int, input().split())
A = []
for _ in range(H):
    line = list(map(int, input().split()))
    A.append(line)

# s[i][j] = [0, i) \times [0, j) の領域の地価の総和
# 0 <= i <= H, 0 <= j <= W
# s[0][0] = 0
# s[i+1][j+1] = s[i+1][j] + s[i][j+1] + A[i][j] - s[i][j]

s = [[0 for j in range(W+1)] for i in range(H+1)]
for i in range(H):
    for j in range(W):
        s[i+1][j+1] = A[i][j]

for i in range(H):
    for j in range(W):
        s[i+1][j+1] += s[i+1][j] + s[i][j+1] - s[i][j]
# pprint(s)

# [i_start, i_end) \times [j_start, j_end) の領域の地価の総和
# 0 <= i_start < i_end <= H, 0 <= j_start < j_end <= W
# s[i_end][j_end] - s[i_start][j_end] - s[i_end][j_start] + s[i_start][j_start]

def can_construct(i_start, i_end, j_start, j_end, V, K):
    cost_buy = s[i_end][j_end] - s[i_start][j_end] - s[i_end][j_start] + s[i_start][j_start]
    cost_build = (i_end - i_start) * (j_end - j_start) * K
    if cost_buy + cost_build <= V:
        return True
    return False

max_area = 0
for i_start in range(H):
    for i_end in range(i_start+1, H+1):
        for j_start in range(W):
            for j_end in range(j_start+1, W+1):
                if not can_construct(i_start, i_end, j_start, j_end, V, K):
                    continue
                max_area = max(max_area, (i_end - i_start) * (j_end - j_start))

print(max_area)
