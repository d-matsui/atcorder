#!/usr/bin/env python3

n, A = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))
# print(n, A, a)

dp = [[False for i in range(A + 1)] for j in range(n + 1)]
# print(dp)

dp[0][0] = True

for i in range(n):
    for j in range(A + 1):
        if j >= a[i]:
            if dp[i][j - a[i]]:
                dp[i + 1][j] = True
        elif dp[i][j]:
            dp[i + 1][j] = True

print(dp[n][A])
