#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
inf = float("inf")

s = input()
t = input()
# print(s, t)

len_s, len_t = len(s), len(t)
max_len = max(len_s, len_t)
dp = [[0 for j in range(max_len + 1)] for i in range(max_len + 1)]

for i in range(len_s):
    for j in range(len_t):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])

# pprint(dp)
# print(dp[len(s)][len(t)])

res = ''
i, j = len_s, len_t
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        # (i - 1, j) -> (i, j)
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        # (i, j - 1) -> (i, j)
        j -= 1
    else:
        # (i - 1, j - 1) -> (i, j)
        res = s[i - 1] + res
        i -= 1
        j -= 1

print(res)
