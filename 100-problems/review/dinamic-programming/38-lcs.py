#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())

for _ in range(N):
    x = list(input())
    y = list(input())

    # dp[i+1][j+1] := xのi文字目までの文字列とyのj文字目までの文字列との最長共通部分列の長さ
    # dp[i+1][j+1] = dp[i][j] + 1 (if x[i] == y[j])
    # dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1]) (if x[i] != y[j])
    dp = [[0 for _ in range(len(y) + 1)] for i in range(len(x) + 1)]

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j], dp[i+1][j], dp[i][j+1])

    print(dp[len(x)][len(y)])
