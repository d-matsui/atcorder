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

    # dp[i + 1][j]: i番目の入力信号を符号化した結果がjとなる場合の、(i番目までの信号の)差の二乗和の最小値
    # y_i = j + C[k]
    # sq_diff = (x[i] - y_i) ** 2
    # dp[i + 1][y_i] = min(dp[i + 1][y_i], dp[i][j] + sq_diff)

    inf = float("inf")
    dp = [[inf for j in range(255 + 1)] for i in range(n_samples + 1)]
    dp[0][128] = 0

    for i in range(n_samples):
        for j in range(255 + 1):
            for k in range(m_codes):
                y_i = j + code_book[k]
                y_i = round_0_255(y_i)
                sq_diff = (input_signal[i] - y_i) ** 2
                dp[i + 1][y_i] = min(dp[i + 1][y_i], dp[i][j] + sq_diff)

    print(min(dp[n_samples]))
