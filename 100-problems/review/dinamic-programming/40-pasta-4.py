#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')
MOD = 10 ** 4


N, K = map(int, input().split())
plans = [-1] * N
for _ in range(K):
    day, menu = map(int, input().split())
    # 0-index
    plans[day-1] = menu - 1

# dp[i][a][b] := i-2日目にパスタa, i-1日目にパスタbを選ぶ予定のうち、条件を満たす予定の数
# 0 <= i <= N - 1
# i日目に選ぶパスタc
# → c = [0, 1, 2] if plans[i] == -1 else plans[i]
# i-1日目にパスタb, i日目にパスタcを選ぶ予定のうち、条件を満たす予定の数
# → dp[i+1][b][c] += dp[i][a][b] (a, b \in [0, 1, 2])

dp = [[[0 for b in range(3)] for a in range(3)] for i in range(N + 1)]

dp[0][0][0] = 1

# for a in range(3):
#     for b in range(3):
#         dp[1][a][b] = 1

for i in range(N):
    for a in range(3):
        for b in range(3):
            c_list = [0, 1, 2] if plans[i] == -1 else [plans[i]]
            for c in c_list:
                if i >= 2 and a == b == c:
                    continue
                dp[i+1][b][c] += dp[i][a][b]

# pprint(dp)
res = 0
for a in range(3):
    for b in range(3):
        res += dp[N][a][b]
print(res % MOD)
