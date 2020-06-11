#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


n, m = map(int, input().split())
coins = list(map(int, input().split()))

# dp[i] := ちょうどi円支払うときのコインの最小枚数

dp = [INF] * (n + 1)
dp[0] = 0

for i in range(n + 1):
    for c in coins:
        if i - c < 0:
            continue
        dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[n])
