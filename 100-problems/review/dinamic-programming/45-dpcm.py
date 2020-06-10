#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


# dp[i+1][j] := i番目の入力信号を復号化した結果がjである場合の、i番目までの信号の差の二乗和の最小値
# i番目の信号を復号化した結果 := y_i = y_{i-1} + C[k_i]
# sq_diff = (x_i - y_i) ** 2
# dp[i+1][j] = min(dp[i+1][j], dp[i][j-C[k_i]] + sq_diff)


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
        code = int(input())
        code_list.append(code)

    input_signal_list = []
    for _ in range(n_samples):
        input_signal = int(input())
        input_signal_list.append(input_signal)

    dp = [[INF for j in range(255 + 1)] for i in range(n_samples + 1)]
    dp[0][128] = 0

    for i in range(n_samples):
        for j in range(255 + 1):
            for c_k in code_list:
                if j < c_k:
                    continue
                sq_diff = (input_signal_list[i] - j) ** 2
                dp[i+1][j] = min(dp[i+1][j], dp[i][round_0_255(j-c_k)] + sq_diff)

    print(min(dp[n_samples]))
