#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')
MAX_NUM = 10 ** 6 - 1


def f(n):
    return n * (n + 1) * (n + 2) // 6


def fill_dp(dp, odd_dp):
    dp[0] = 0
    odd_dp[0] = 0

    for x in range(MAX_NUM + 1):
        for i in range(1, MAX_NUM):
            if x - f(i) < 0:
                break
            dp[x] = min(dp[x], dp[x-f(i)] + 1)
            if f(i) % 2 == 1:
                odd_dp[x] = min(odd_dp[x], odd_dp[x-f(i)] + 1)
    return dp, odd_dp


# dp[x] := 整数xを表現するのに必要な正四面体数の最小個数
# dp[x] = min(dp[x], dp[x-f(i)] + 1) (x - f(i) >= 0, i \in [1, 2, ...])
dp = [INF for x in range(MAX_NUM + 1)]
odd_dp = [INF for x in range(MAX_NUM + 1)]
dp, odd_dp = fill_dp(dp, odd_dp)

while True:
    num = int(input())
    if num == 0:
        break
    print(dp[num], odd_dp[num])
