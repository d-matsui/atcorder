#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
A = list(map(int, input().split()))

# dp[i] := i日目の売却時の所持金の最大
# dp[i] = max(i-1のまま, j日目時点で買えるだけ買った株全て売却)

dp = [0] * (N+1)
dp[0] = 1000

for i in range(1, N+1):
    # print(f'i = {i}')
    max_j = 0
    for j in range(1, i):
        # print(f'j = {j}')
        q, r = divmod(dp[j-1], A[j-1])
        # print(f'q, r = {q}, {r}')
        max_j = max(max_j, A[i-1] * q + r)
    # print(f'dp[i-1] = {dp[i-1]}, max_j = {max_j}')
    dp[i] = max(dp[i-1], max_j)

# pprint(dp)
print(dp[N])
