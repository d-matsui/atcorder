#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

# dp[i + 1][j]: 重さjを超えないようiまでの品物から重複を許して品物を選んだときの価値の最大値
# dp[i + 1][j]を以下の3つのmax()を取って計算
# iを選ばない: dp[i][j]
# 重複せずiを選ぶ: dp[i][j - weight[i]] + value[i]
# 重複してiを選ぶ: dp[i + 1][j - weight[i]] + value[i]

N, W = map(int, input().split())
value = []
weight = []
for _ in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

inf = float("inf")
dp = [[-inf for j in range(W + 1)] for i in range(N + 1)]

for i in range(N):
    dp[i][0] = 0

for j in range(W + 1):
    dp[0][j] = 0

for i in range(N):
    for j in range(W + 1):
        if j - weight[i] >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i], dp[i + 1][j - weight[i]] + value[i])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])
