#!/usr/bin/env python3

# dp[0] = 0
# dp[i + 1] = max(dp[i], dp[i] + a[i])

n = int(input())
a = list(map(int, input().split()))

dp = {}

dp[0] = 0
for i in range(n):
    dp[i + 1] = max(dp[i], dp[i] + a[i])

print(dp[n])
