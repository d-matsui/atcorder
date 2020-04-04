#!/usr/bin/env python3

n, m = map(int, input().split())
coins = list(map(int, input().split()))

inf = float("inf")
# dp[i + 1][j]: i番目までのコインを使ってj円払うときのコインの最小枚数
# dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - coins[i]] + 1)
dp = [[inf for _ in range(n + 1)] for i in range(m + 1)]

dp[0][0] = 0

for i in range(m):
    for price in range(n + 1):
        if price - coins[i] >= 0:
            dp[i + 1][price] = min(dp[i][price], dp[i + 1][price - coins[i]] + 1)
        else:
            dp[i + 1][price] = min(dp[i + 1][price], dp[i][price])

print(dp[m][n])
