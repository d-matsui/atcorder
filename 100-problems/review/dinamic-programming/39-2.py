#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


N = int(input())
numbers = list(map(int, input().split()))

# dp[i+1][j] := i個目までの数字と、+, -を使ってできた数式の和がjであるような等式の数
# 0 <= i <= N-1
# dp[i+1][j] = dp[i][j+numbers[i]] + dp[i][j-numbers[i]]
# res = dp[N-1][numbers[N-1]]

MAX_NUM = 20
dp = [[0 for j in range(MAX_NUM + 1)] for i in range(N + 1)]
dp[1][numbers[0]] = 1

for i in range(N):
    for j in range(MAX_NUM + 1):
        if 0 <= j + numbers[i] <= MAX_NUM:
            dp[i+1][j] += dp[i][j+numbers[i]]
        if 0 <= j - numbers[i] <= MAX_NUM:
            dp[i+1][j] += dp[i][j-numbers[i]]

print(dp[N-1][numbers[N-1]])
