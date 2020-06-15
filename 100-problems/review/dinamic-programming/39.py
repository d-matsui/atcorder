#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


n = int(input())
numbers = list(map(int, input().split()))

# dp[i+1][j] := 左からi番目までの数字と+, - を使って作った式の計算結果がjであるような式の数
# dp[i+1][j] += dp[i][j+a[i]] + dp[i][j-a[i]]

MAX = 20
dp = [[0 for j in range(MAX + 1)] for i in range(n + 1)]
dp[1][numbers[0]] = 1

for i in range(n):
    for j in range(MAX + 1):
        if 0 <= j + numbers[i] <= MAX:
            dp[i+1][j] += dp[i][j+numbers[i]]
        if 0 <= j - numbers[i] <= MAX:
            dp[i+1][j] += dp[i][j-numbers[i]]
print(dp[n-1][numbers[-1]])
