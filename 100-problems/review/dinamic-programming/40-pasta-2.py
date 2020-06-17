#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 4


N, K = map(int, input().split())

sched = [-1] * N
for _ in range(K):
    day, kind = map(int, input().split())
    sched[day-1] = kind - 1
# pprint(sched)

# dp[i+1][a][b] := i-2日目の予定がa, i-1日目の予定がbであるときのi日目の予定(c)として成り立つパターン数
# dp[i+1][a][b] += dp[i][b][c] (not a == b == c)
# 2 <= i <= N, a, b, c \n {0, 1, 2}

dp = [[[0 for b in range(3)] for a in range(3)] for i in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    for a in range(3):
        for b in range(3):
            c_list = [0, 1, 2] if sched[i] == -1 else [sched[i]]
            for c in c_list:
                if i >= 2 and a == b == c:
                    continue
                dp[i+1][b][c] += dp[i][a][b]

res = 0
for a in range(3):
    for b in range(3):
        res += dp[N][a][b]
print(res % MOD)
