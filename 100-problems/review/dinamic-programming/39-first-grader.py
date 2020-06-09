#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n = int(input())
numbers = list(map(int, input().split()))

# dp[i+1][j] := i番目までの数字と+, -で作った式の計算結果がjであるような式の数
# 0 <= i <= n - 2, 0 <= j <= 20
# dp[i+1][j] = max(dp[i][j], dp[i][j+a[i]], dp[i][j-a[i]])

# dp = [[0 for j in range(21)] for i in range(n)]

# dp[1][numbers[0]] = 1

# for i in range(n - 1):
#     for j in range(21):
#         if dp[i][j] > 0:
#             plus = j + numbers[i]
#             minus = j - numbers[i]
#             if 0 <= plus <= 20:
#                 dp[i+1][plus] += dp[i][j]
#             if 0 <= minus <= 20:
#                 dp[i+1][minus] += dp[i][j]

# print(dp[n-1][numbers[-1]])

# dp[i][j] := 左からi個の穴それぞれに+, -を入れた式の計算結果がjである式の数
# a_0 + a_1 + ... + a_k
# 0 <= i <= n - 2, 0 <= j <= 20
# dp[i][j] = dp[i-1][j+a[i]] + dp[i-1][j-a[i]]

dp = [[0 for j in range(21)] for i in range(n - 1)]

dp[0][numbers[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        plus = j + numbers[i]
        minus = j - numbers[i]
        if 0 <= plus <= 20:
            dp[i][j] += dp[i-1][plus]
        if 0 <= minus <= 20:
            dp[i][j] += dp[i-1][minus]

print(dp[n-2][numbers[-1]])
