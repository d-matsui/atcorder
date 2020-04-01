#!/usr/bin/env python3

N = int(input())

a = []
for i in range(N):
    line = list(map(int, input().split()))
    a.append(line)

# dp[i + 1][j]: i日目にjを選んだ場合の幸福度の最大値
# dp[i + 1][j] = max(dp[i][k_1], dp[i][k_2])
# ただし、k_1, k_2 != j and k_1 != k_2

inf = float("inf")
n_pattern = 3
dp = [[-inf for _ in range(n_pattern)] for i in range(N + 1)]

for i in range(n_pattern):
    dp[0][i] = 0

for i in range(N):
    for j in range(n_pattern):
        for k in range(n_pattern):
            if k != j:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] + a[i][j])

print(max(dp[N]))
