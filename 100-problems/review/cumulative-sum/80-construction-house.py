#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


H, W, K, V = map(int, input().split())
A = []
for _ in range(H):
    line = list(map(int, input().split()))
    A.append(line)

# s[i][j] := [0, 0] ~ [i-1, j-1]の土地に家を建てるのに必要な金額
# s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + A[i][j]
s = [[0 for j in range(W+1)] for i in range(H+1)]

for i in range(H):
    for j in range(W):
        s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + A[i][j]
# pprint(s)


def calc_cost(p_i, p_j, q_i, q_j):
    cost_land = s[q_i][q_j] - s[q_i][p_j] - s[p_i][q_j] + s[p_i][p_j]
    cost_build = (q_i - p_i) * (q_j - p_j) * K
    return cost_land + cost_build


max_area = 0
# p_i < q_i, p_j < q_j
for p_i in range(H):
    for p_j in range(W):
        for q_i in range(p_i+1, H+1):
            for q_j in range(p_j+1, W+1):
                cost = calc_cost(p_i, p_j, q_i, q_j)
                if cost <= V:
                    max_area = max(max_area, (q_i - p_i) * (q_j - p_j))

print(max_area)
