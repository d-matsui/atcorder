#!/usr/bin/env python3

q = int(input())
X = []
Y = []

for i in range(q):
    line = list(input())
    X.append(line)
    line = list(input())
    Y.append(line)
# print(q, X, Y)


def init_dp(x, y):
    inf = float("inf")
    dp = [[-inf for i in range(len(y))] for j in range(len(x))]
    for i in range(len(x)):
        if y[0] == x[i]:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    for i in range(len(y)):
        if x[0] == y[i]:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    return dp


# dp[i][j]: 文字列x[:i]と文字列y[:j]の最長共通部分の長さ
# x[i] == y[j]のとき、dp[i][j] = dp[i - 1][j - 1] + 1
# x[i] != y[j]のとき、dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

def fill_dp_lcs(dp, x, y):
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def lcs_str(dp, x, y):
    i, j = len(x) - 1, len(y) - 1
    lcs = dp[i][j]
    lcs_str = ''
    while i >= 0 and j >= 0:
        if x[i] == y[j]:
            lcs_str += x[i]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] == lcs:
                i -= 1
            else:
                j -= 1
    return ''.join(list(reversed(lcs_str)))


for i in range(q):
    x, y = X[i], Y[i]
    dp = init_dp(x, y)
    dp = fill_dp_lcs(dp, x, y)
    print(dp[len(x) - 1][len(y) - 1])
    # res = lcs_str(dp, x, y)
    # print(res)
