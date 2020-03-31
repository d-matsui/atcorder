#!/usr/bin/env python3

n = int(input())
h = list(map(int, input().split()))
# print(n, h)

dp = [-1 for _ in range(n)]

dp[0], dp[1] = 0, abs(h[1] - h[0])

for i in range(2, n):
    one_step = dp[i - 1] + abs(h[i] - h[i - 1])
    two_step = dp[i - 2] + abs(h[i] - h[i - 2])
    dp[i] = min(one_step, two_step)

print(dp[n - 1])
