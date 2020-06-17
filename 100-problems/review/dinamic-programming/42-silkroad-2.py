#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n_towns, m_days = map(int, input().split())
# d_0 = None
dist = [None]
for _ in range(n_towns):
    d = int(input())
    dist.append(d)
weather = [None]
# w_0 = None
for _ in range(m_days):
    w = int(input())
    weather.append(w)

# dp[i][j] := i日目に都市jに到着 or 滞在したときの疲労度の合計の最小値
# i日目に到着, i-1日目にjに到着してi日目に滞在、
# dp[i][j] = min(dp[i-1][j-1] + weather[i] * dist[j], dp[i-1][j])

dp = [[INF for j in range(n_towns + 1)] for i in range(m_days + 1)]
for i in range(m_days + 1):
    dp[i][0] = 0

for i in range(1, m_days + 1):
    for j in range(1, n_towns + 1):
        dp[i][j] = min(dp[i-1][j-1] + dist[j] * weather[i], dp[i-1][j])

# pprint(dp)
res = INF
for i in range(1, m_days + 1):
    res = min(res, dp[i][n_towns])
print(res)
