#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')
MOD = 10 ** 4


N, K = map(int, input().split())

sched = [None] * N
for _ in range(K):
    day, kind = map(int, input().split())
    sched[day-1] = kind - 1

dp = [[[0 for q in range(3)] for p in range(3)] for i in range(N + 1)]

dp[0][0][0] = 1

for i in range(N):
    for a in range(3):
        for b in range(3):
            c_list = [0, 1, 2] if sched[i] is None else [sched[i]]
            for c in c_list:
                if i >= 2 and a == b == c:
                    continue
                dp[i+1][b][c] += dp[i][a][b]

res = 0
for a in range(3):
    for b in range(3):
        res += dp[N][a][b]
print(res % MOD)
