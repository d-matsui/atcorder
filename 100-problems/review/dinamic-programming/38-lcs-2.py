#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n = int(input())

for _ in range(n):
    x = list(input())
    y = list(input())
    len_x = len(x)
    len_y = len(y)

    # dp[i+1][j+1] := xのi番目までの文字列とyのj番目までの文字列から成る最長共通部分列の長さ
    # dp[i+1][j+1] = dp[i][j] + 1 (if x[i] == y[j])
    # dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1]) (if x[i] != y[j])

    dp = [[0 for j in range(len_y + 1)] for i in range(len_x + 1)]

    for i in range(len_x):
        for j in range(len_y):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    # pprint(dp)
    print(dp[len_x][len_y])
