#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


d_days, n_clothes = map(int, input().split())

temp_list = []
for _ in range(d_days):
    temp = int(input())
    temp_list.append(temp)

clothes_list = []
for _ in range(n_clothes):
    a, b, c = map(int, input().split())
    clothes_list.append([a, b, c])

# dp[i+1][j] := i 日目に服 j を着たときの服の派手さの差の絶対値和の最大値
# dp[i+1][j] = max(dp[i+1][j], dp[i][k] + abs(c_k - c_j))
# 0 <= i <= d_days, 0 <= j <= n_clothes - 1
# c_j は a_j <= temp_list[i] <= b_j を満たす
# c_k は a_k <= temp_list[i-1] <= b_k を満たす

dp = [[0 for j in range(n_clothes)] for i in range(d_days + 1)]

for i in range(1, d_days):
    for j in range(n_clothes):
        a_j, b_j, c_j = clothes_list[j]
        if not a_j <= temp_list[i] <= b_j:
            continue
        for k in range(n_clothes):
            a_k, b_k, c_k = clothes_list[k]
            if not a_k <= temp_list[i-1] <= b_k:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][k] + abs(c_k - c_j))

print(max(dp[d_days]))
