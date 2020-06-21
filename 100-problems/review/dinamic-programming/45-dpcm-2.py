#!/usr/bin/env python3

# TLE and NG
# 5 1
# 255
# 0
# 0
# 0
# 0
# 0

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


def round_0_255(n):
    if n < 0:
        return 0
    if n > 255:
        return 255
    return n


while True:
    n_samples, m_codes = map(int, input().split())
    if n_samples == 0 and m_codes == 0:
        break

    code_list = []
    for _ in range(m_codes):
        c = int(input())
        code_list.append(c)

    x_list = []
    for _ in range(n_samples):
        x = int(input())
        x_list.append(x)

    # dp[i+1][j] := i番目の入力信号の復号結果がjとなるよう圧縮したときの、入力信号と復号化後の信号との差の二乗和の最小値
    # 0 <= i <= n_samples - 1
    # y[i] = y[i-1] + C[k]より、
    # j = y[i-1] + C[k]だから、y[i-1] = j - C[k]
    # コードブックの各要素を用いて復号(圧縮?)した場合を全て試して、dpを更新する
    # dp[i+1][j] = min(dp[i+1][j], dp[i][j-c[k]] + abs(x_list[i] - j) ** 2
    # k \in code_list, j-c[k] >= 0
    dp = [[INF for j in range(255 + 1)] for i in range(n_samples + 1)]
    dp[0][128] = 0

    for i in range(n_samples):
        for j in range(255 + 1):
            for c_k in code_list:
                diff = (x_list[i] - j) ** 2
                dp[i+1][j] = min(dp[i+1][j], dp[i][round_0_255(j - c_k)] + diff)
    print(min(dp[n_samples]))
