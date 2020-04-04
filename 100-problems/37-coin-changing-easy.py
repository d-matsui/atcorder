#!/usr/bin/env python3

n, m = map(int, input().split())
coins = list(map(int, input().split()))

inf = float("inf")
# dp[i][j]: i番目までのコインを使ってj円払うときのコインの最小枚数
# dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)
dp = [[inf for _ in range(n + 1)] for i in range(m)]

for i in range(m):
    dp[i][0] = 0
for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m):
    for price in range(1, n + 1):
        if price - coins[i] >= 0:
            dp[i][price] = min(dp[i - 1][price], dp[i][price - coins[i]] + 1)
        else:
            dp[i][price] = min(dp[i][price], dp[i - 1][price])

print(dp[m - 1][n])
