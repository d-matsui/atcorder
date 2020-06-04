#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')

n = int(input())
str_list = []
for _ in range(n):
    x = list(input())
    y = list(input())
    str_list.append([x, y])
# pprint(str_list)

# dp[i+1][j+1] := Xの左からi文字切り出した部分文字列と、Yの左からj文字切り出した部分文字列との共通部分文字列長
# dp[i+1][j+1] = dp[i][j] + 1 (if X[i] == Y[j])
# dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]) (if not X[i] == Y[j])


def lcs(x, y):
    len_x = len(x)
    len_y = len(y)
    dp = [[0 for j in range(len_y + 1)] for i in range(len_x + 1)]

    for i in range(len_x):
        for j in range(len_y):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[len_x][len_y]


for i in range(n):
    x, y = str_list[i]
    print(lcs(x, y))
