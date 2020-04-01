# #!/usr/bin/env python3

N, W = map(int, input().split())

weight = []
value = []
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
# print(N, W)
# print(weight, value)

max_sum_v = N * 1000
inf = float("inf")
dp = [[inf for i in range(max_sum_v + 1)] for j in range(N + 1)]

# for i in range(max_sum_v + 1):
#     dp[0][i] = 0

dp[0][0] = 0

# # dp[i + 1][sum_v]: i番目までの品物から価値がsum_v以上になるように選んだときの、重さの総和の最小値
# # dp[i + 1][sum_v] = max(dp[i][sum_v], dp[i][sum_v - v[i]] + w[i])

for i in range(N):
    for sum_v in range(max_sum_v + 1):
        if sum_v - value[i] >= 0:
            dp[i + 1][sum_v] = min(dp[i][sum_v], dp[i][sum_v - value[i]] + weight[i])
        else:
            dp[i + 1][sum_v] = dp[i][sum_v]

for sum_v in range(max_sum_v + 1):
    if dp[N][sum_v] <= W:
        res = sum_v

print(res)
