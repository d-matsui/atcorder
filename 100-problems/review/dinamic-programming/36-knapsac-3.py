#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


N, W = map(int, input().split())
v_list = []
w_list = []
for _ in range(N):
    v, w = map(int, input().split())
    v_list.append(v)
    w_list.append(w)

# dp[w] := 重さがwを超えないように品物をいくつか選んだときの価値の和の最大値
# dp[w] = max(dp[w], dp[w-w_list[i]] + v_list[i])

dp = [0 for w in range(W + 1)]

for w in range(1, W + 1):
    for i in range(N):
        if w - w_list[i] < 0:
            continue
        dp[w] = max(dp[w], dp[w-w_list[i]] + v_list[i])

# pprint(dp)
print(dp[W])
