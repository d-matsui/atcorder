#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A = A + A

# dp[start][end]: 残り[start][end]からスタートしたときのJOIの取り分の最大値
# JOIが取るとき
# dp[start][end] = max(dp[start + 1][end] + A[start], dp[start][end - 1] + A[end])
# IOIが取るとき
# dp[start][end] = dp[start + 1][end] (A[start] > A[end])
# dp[start][end] = dp[start][end - 1] (A[end] > A[start])

dp = [[0 for end in range(2 * N + 1)] for start in range(2 * N + 1)]

res = 0
for start in range(N):
    for end in range(2 * N - start):
        k = start + end
        if (N - start) % 2 == 1:
            dp[end][k] = max(dp[end + 1][k] + A[end], dp[end][k - 1] + A[k])
        else:
            if A[k] > A[end]:
                dp[end][k] = dp[end][k - 1]
            else:
                dp[end][k] = dp[end + 1][k]
        if start == N - 1:
            res = max(res, dp[end][k])

print(res)
