#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
coins = list(map(int, input().split()))

# dp[i + 1][j]: i番目までのコインを使ってj円払うときのコイン枚数の最小値
# dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - coins[i]] + 1)

inf = float("inf")
dp = [[inf for j in range(n + 1)] for i in range(m + 1)]

dp[0][0] = 0

for i in range(m):
    for j in range(n + 1):
        if j - coins[i] >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - coins[i]] + 1)
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])

print(dp[m][n])
