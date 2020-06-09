#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')
MOD = 10 ** 4


n_days, k_plans = map(int, input().split())
sched = [-1] * n_days
for _ in range(k_plans):
    day, kind = map(int, input().split())
    sched[day-1] = kind - 1
# pprint(sched)

# dp[i+1][a][b] := i-2日目の予定がa, i-1日目の予定がbであるときの、i日目の予定として成り立つパターンの数
# i日目の予定をcとおき、cの取り得る値全てに対し、その予定が成り立つかを調べる。
# not a == b == c であれば、i日目の予定cは成り立つ。
# 2 <= i <= n, a, b, c \in {0, 1, 2}

dp = [[[0 for b in range(3)] for a in range(3)] for i in range(n_days + 1)]

dp[0][0][0] = 1

for i in range(n_days):
    for a in range(3):
        for b in range(3):
            c_list = [0, 1, 2] if sched[i] == -1 else [sched[i]]
            for c in c_list:
                if i >= 2 and a == b == c:
                    continue
                dp[i+1][b][c] += dp[i][a][b]

res = 0
for i in range(3):
    for j in range(3):
        res += dp[n_days][i][j]
print(res % MOD)
