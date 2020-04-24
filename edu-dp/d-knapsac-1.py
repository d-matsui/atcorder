#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

n_item, w_volume = map(int, input().split())
weight, value = [], []
for _ in range(n_item):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
# print(n_item, w_volume, weight, value)

# dp[i + 1][w]: i番目までの商品から重さがwを超えないよういくつか選んだときの価値の最大値
# 商品iを選ぶことができるとき (w - weight[i] >= 0 のとき)
# dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
# 商品iを選ぶことができないとき
# dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

dp = [[0 for w in range(w_volume + 1)] for i in range(n_item + 1)]

for i in range(n_item):
    for w in range(w_volume + 1):
        if w - weight[i] >= 0:
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
        dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

print(dp[n_item][w_volume])
