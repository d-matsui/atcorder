#!/usr/bin/env python3

N, K = map(int, input().split())

h = list(map(int, input().split()))
# print(N, K, h)

inf = float("inf")
dp = [inf for _ in range(N)]

dp[0] = 0

# 配るDP
# for i in range(N):
#     for k in range(1, K + 1):
#         if i + k < N:
#             k_step = dp[i] + abs(h[i] - h[i + k])
#             dp[i + k] = min(dp[i + k], k_step)

# 貰うDP
for i in range(1, N):
    for k in range(1, K + 1):
        if i - k >= 0:
            k_step = dp[i - k] + abs(h[i - k] - h[i])
            dp[i] = min(dp[i], k_step)

print(dp[N - 1])
