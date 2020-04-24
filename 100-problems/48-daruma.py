#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

while True:
    n = int(input())
    if n == 0:
        break
    weight = list(map(int, input().split()))
    # print(n, w)
    dp = [[0 for i in range(n)] for j in range(n)]

    for w in range(2, n + 1):
        for l in range(n):
            r = l + w - 1
            if r >= n:
                continue
            if dp[l + 1][r - 1] == w - 2 and abs(weight[l] - weight[r]) <= 1:
                dp[l][r] = w
            for k in range(l, r):
                dp[l][r] = max(dp[l][r], dp[l][k] + dp[k + 1][r])
    print(dp[0][n - 1])
