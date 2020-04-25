#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

N = int(input())
A = list(map(int, input().split()))

# cumulative sum
# s_{i+1} = s_i + a_i, s_0 = 0
# 区間 [left, right) の総和 = s[right] - s[left]
cum_sum = [0 for _ in range(N + 1)]
for i in range(N):
    cum_sum[i + 1] = cum_sum[i] + A[i]
# print(cum_sum)

res = []
for k in range(1, N + 1):
    max_sum = 0
    for left in range(N):
        right = left + k
        if right <= N:
            max_sum = max(max_sum, cum_sum[right] - cum_sum[left])
    res.append(max_sum)

for r in res:
    print(r)
