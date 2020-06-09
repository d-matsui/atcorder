#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_towns, m_days = map(int, input().split())

d_list = []
for _ in range(n_towns):
    d = int(input())
    d_list.append(d)

weather_list = []
for _ in range(m_days):
    weather = int(input())
    weather_list.append(weather)

# dp[i][j] := i日目に都市jに移動 or 待機したときの疲労度の最小値
# dp[i][j] = min(dp[i][j], dp[i-1][j-1] + d[i] * c[i], dp[i-1][j])

dp = [[INF for j in range(n_towns + 1)] for i in range(m_days + 1)]

for i in range(n_towns + 1):
    dp[i][0] = 0

for i in range(m_days + 1):
    for j in range(n_towns + 1):
        if i >= j and i > 0:
            c = weather_list[i-1]
            d = d_list[j-1]
            dp[i][j] = min(dp[i-1][j-1] + d * c, dp[i-1][j])

# pprint(dp)

res = INF
for i in range(n_towns, m_days + 1):
    res = min(res, dp[i][n_towns])
print(res)
