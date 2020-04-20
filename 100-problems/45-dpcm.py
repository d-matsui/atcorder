#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline


def round_0_255(num):
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else:
        return num


while True:
    n_samples, m_codes = map(int, input().split())
    if n_samples == 0 and m_codes == 0:
        break

    code_book = []
    for _ in range(m_codes):
        code_book.append(int(input()))

    input_signal = []
    for _ in range(n_samples):
        input_signal.append(int(input()))

    # print(code_book, input_signal)

    # dp[i + 1][j]: i番目の入力信号を復号した結果がjとなる場合の、(i番目までの信号の)差の二乗和の最小値
    # i番目の入力信号を復号した結果をy_iとすると、y_iは以下で与えられる
    # y_i = y_{i-1} + C[k_i]
    # sq_diff = (x[i] - y_i) ** 2
    # dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - C[k_i]] + sq_diff)

    inf = float("inf")
    dp = [[inf for j in range(255 + 1)] for i in range(n_samples + 1)]
    dp[0][128] = 0

    for i in range(n_samples):
        for j in range(255 + 1):
            for c_k in code_book:
                sq_diff = (input_signal[i] - j) ** 2
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][round_0_255(j - c_k)] + sq_diff)
    # print(dp[n_samples])
    print(min(dp[n_samples]))
