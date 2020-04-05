#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
# print(n, a)

# dp[i + 1][j]: i番目までの数字と+, -を使った式の計算結果 (部分和) がjになるようなパターン数
# n - 1個演算に使える数字があるので、0 <= i <= n - 2 (n - 1通り)
# 部分和は0以上20以下であるので、0 <= j <= 20 (21通り)

dp = [[0 for j in range(21)] for i in range(n)]

dp[1][a[0]] += 1

for i in range(n - 1):
    for j in range(21):
        if dp[i][j] > 0:
            plus = j + a[i]
            minus = j - a[i]
            if plus >= 0 and plus <= 20:
                dp[i + 1][plus] += dp[i][j]
            if minus >= 0 and minus <= 20:
                dp[i + 1][minus] += dp[i][j]

print(dp[n - 1][a[n - 1]])
