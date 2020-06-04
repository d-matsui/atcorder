#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_yen, m_coins = map(int, input().split())
coins = list(map(int, input().split()))

# dp[i] := i円支払うときのコインの最小枚数
# dp[i] = min(dp[i], dp[i - coin[j]]) (i - coin[j] >= 0)
dp = [INF] * (n_yen + 1)
dp[0] = 0

for i in range(1, n_yen + 1):
    for j in range(m_coins):
        if i - coins[j] >= 0:
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

print(dp[n_yen])
