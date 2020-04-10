#!/usr/bin/env python3

# g[n]: n番目の正四面体数
# g[n] = n * (n + 1) * (n + 2) / 6
# dp[x]: xを表現するのに必要な正四面体数の個数の最小値
# dp[x] = min(dp[x - g(1)], dp[x - g(2)], ..., dp[x - g[i]]) + 1
# ただし、iはx <= g[i]を満たす最大の整数


def g(n):
    return n * (n + 1) * (n + 2) // 6


def fill_dp(dp, odddp):
    i = 1
    while True:
        g_i = g(i)
        if g_i >= max_num:
            break
        for x in range(g_i, max_num):
            dp[x] = min(dp[x], dp[x - g_i] + 1)
            if g_i % 2 == 1:
                odddp[x] = min(odddp[x], odddp[x - g_i] + 1)
        i += 1
    return dp, odddp


max_num = 10 ** 6
dp = [max_num for _ in range(max_num + 1)]
odddp = [max_num for _ in range(max_num + 1)]

dp[0] = 0
odddp[0] = 0
dp, odddp = fill_dp(dp, odddp)

while True:
    num = int(input())
    if num == 0:
        break
    print(dp[num], odddp[num])
