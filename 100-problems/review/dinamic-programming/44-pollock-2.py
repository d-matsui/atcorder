#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MAX_NUM = 10 ** 6

# dp[x] := 整数xを作るのに必要な正四面体数の個数の最小値
# f(n) := n番目の正四面体数
# dp[x] = min(dp[x], dp[x - f(i)] + 1) (x - f(i) >= 0)


def f(n):
    return n * (n+1) * (n+2) // 6


def fill_dp(dp, dp_odd):
    i = 1
    while True:
        if f(i) >= MAX_NUM:
            break
        for x in range(f(i), MAX_NUM):
            dp[x] = min(dp[x], dp[x - f(i)] + 1)
            if f(i) % 2 == 1:
                dp_odd[x] = min(dp_odd[x], dp_odd[x - f(i)] + 1)
        i += 1
    return dp, dp_odd


dp = [INF for x in range(MAX_NUM+1)]
dp_odd = [INF for x in range(MAX_NUM+1)]
dp[0] = 0
dp_odd[0] = 0

dp, dp_odd = fill_dp(dp, dp_odd)

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n], dp_odd[n])
