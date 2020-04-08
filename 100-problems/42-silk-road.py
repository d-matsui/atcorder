#!/usr/bin/env python3

n_cities, m_days = map(int, input().split())

d = []
for _ in range(n_cities):
    d.append(int(input()))

w = []
for _ in range(m_days):
    w.append(int(input()))

# dp[i][j]: i日目にjへ移動or滞在したときの疲労度の最小値
# dp[i][j] = min(dp[i - 1][j - 1] + d[j] * w[i], dp[i - 1][j])
# 0 < i <= m_days, 0 < j <= n_cities

inf = float("inf")
dp = [[inf for city in range(n_cities + 1)] for day in range(m_days + 1)]

# 都市0からスタート
for day in range(m_days + 1):
    dp[day][0] = 0

for day in range(m_days + 1):
    for city in range(n_cities + 1):
        if day >= city and day > 0:
            dp[day][city] = min(dp[day - 1][city - 1] + d[city - 1] * w[day - 1], dp[day - 1][city])

# print(dp)

min_days = n_cities
max_days = m_days + 1

min_cost = inf
for day in range(min_days, max_days):
    min_cost = min(min_cost, dp[day][n_cities])

print(min_cost)
