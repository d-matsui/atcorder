#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

N, W = map(int, input().split())
value = []
weight = []
for _ in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)
# print(value, weight)

inf = float("inf")
dp = [0 for _ in range(W + 1)]

for i in range(N):
    for w in range(W + 1):
        if w - weight[i] >= 0:
            dp[w] = max(dp[w], dp[w - weight[i]] + value[i])

print(dp[W])
