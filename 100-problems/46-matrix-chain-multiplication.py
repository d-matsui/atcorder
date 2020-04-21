#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n = int(input())
l_dim = []
for _ in range(n):
    row, col = map(int, input().split())
    l_dim.append([row, col])
# print(l_dim)

# dp[left][right]: M_left M_{left+1} ... M_rightのスカラー乗算回数の最小値
# 行列 M_left と行列 M_right のスカラー乗算回数: row_left * col_right * col_left
# 行列 M_left ... M_k と行列 M_{k+1} ... M_right の積を考え、最小値を更新していく
# dp[left][right]: min(dp[left][right], dp[M_left][M_k] + dp[M_{k+1}][M_right] + row_left * col_right * col_k)
# ただし、left <= k <= right

dp = [[-1 for j in range(n)] for i in range(n)]


def rec_dp(left, right):
    if dp[left][right] >= 0:
        # 既に最小値が決まっている
        return dp[left][right]
    if left == right:
        # dp[i][i] = 0
        return 0

    row_left = l_dim[left][0]
    col_right = l_dim[right][1]
    res = float("inf")
    for k in range(left, right):
        col_k = l_dim[k][1]
        num = row_left * col_right * col_k
        res = min(res, rec_dp(left, k) + rec_dp(k + 1, right) + num)
    dp[left][right] = res

    return dp[left][right]


print(rec_dp(0, n - 1))
