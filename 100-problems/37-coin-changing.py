#!/usr/bin/env python3

n, m = map(int, input().split())
coins = list(map(int, input().split()))
# print(n, m, coins)

inf = float("inf")
dp = [inf for _ in range(n + 1)]
dp[0] = 0

# dp[price]: 金額がpriceを超えないようコインをいくつか選んだときのコインの枚数の最小値
# 金額がpriceを超えないよう 0, ..., i のコインをいくつか選んだときの、コインの枚数の最小値を更新していく
# dp[price] = max(dp[price], dp[price - coins[i]] + 1)

for coin in coins:
    for price in range(n + 1):
        if price - coin >= 0:
            dp[price] = min(dp[price], dp[price - coin] + 1)

print(dp[n])
