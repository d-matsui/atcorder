#!/usr/bin/env python3

# dp[i + 1][w] := i番目までの品物の中から重さがwを超えないように選んだときの、価値の総和の最大値
# 品物を選ぶとき: dp[i + 1][w] = dp[i][w - weigth[i]] + value[i]
# 品物を選ばないとき: dp[i + 1][w] = dp[i][w]

N, W = map(int, input().split())

goods = []
for _ in range(N):
    v, w = map(int, input().split())
    goods.append([v, w])
# print(goods)

inf = float("inf")
dp = [[-inf for _ in range(W + 1)] for j in range(N + 1)]
# print(dp)

for w in range(W):
    dp[0][w] = 0

for i in range(N):
    for w in range(W + 1):
        if w >= goods[i][1]:
            dp[i + 1][w] = max(dp[i][w - goods[i][1]] + goods[i][0], dp[i][w])
        else:
            dp[i + 1][w] = dp[i][w]

print(dp[N][W])
