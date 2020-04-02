#!/usr/bin/env python3

N, W = map(int, input().split())

v_list, w_list = [], []
for i in range(N):
    v_i, w_i = map(int, input().split())
    v_list.append(v_i)
    w_list.append(w_i)
# print(N, W)
# print(v_list, w_list)

# dp[w]: 重さの和がwを超えないよう品物を選んだときの、価値の和の最大値
# 重さの和がwを超えないよう、0, ..., iの品物をいくつか選んだときの、価値の最大の和を更新していく
# dp[w] = max(dp[w], dp[w - w_list[i] + v_list[i]])

dp = [0 for _ in range(W + 1)]

for i in range(N):
    for w in range(W + 1):
        if w - w_list[i] >= 0:
            dp[w] = max(dp[w], dp[w - w_list[i]] + v_list[i])

print(dp[W])
