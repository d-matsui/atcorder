#!/usr/bin/env python3

days, n = map(int, input().split())
l_temp = []
for _ in range(days):
    l_temp.append(int(input()))
clothing = []
for _ in range(n):
    a, b, c = map(int, input().split())
    clothing.append([a, b, c])
# print(days, n)
# print(l_temp, clothing)

# dp[i + 1][j]: i日目にjを着たときの、派手さの差の絶対値和の最大値
# dp[i + 1][j] = max(dp[i][k] + abs(c_k - c_j))
# 1 <= i <= days, 1 <= j <= nである
# ただし、a_j <= l_temp[i] <= b_j であり、a_k <= l_temp[i - 1] <= b_kを満す

inf = float("inf")
dp = [[0 for j in range(n)] for i in range(days + 1)]
# print(dp)

for i in range(1, days):
    for j in range(n):
        a_j, b_j, c_j = clothing[j]
        if a_j <= l_temp[i] <= b_j:
            for k in range(n):
                a_k, b_k, c_k = clothing[k]
                if a_k <= l_temp[i - 1] <= b_k:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] + abs(c_k - c_j))

print(max(dp[days]))
