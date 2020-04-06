#!/usr/bin/env python3

# 3 <= n <= 100
# 1 <= k <= n

n, k = map(int, input().split())
sched = []
for _ in range(k):
    a, b = map(int, input().split())
    sched.append([a, b])
# print(n, k, sched)

sched_all = [-1 for _ in range(n)]
for i, menu in sched:
    sched_all[i - 1] = menu - 1
# print(sched_all)

# dp[i][a][b]: i - 2日目がa, i - 1日目がbであるような予定の個数
# i日目が既に決まっていれば、その予定cをi日目の予定とする
# 決まっていなければ、c in [0, 1, 2]を全て試す
# i >= 2のみを考え、not a == b == c なら、その予定は成り立つ

dp = [[[0 for b in range(3)] for a in range(3)] for i in range(n + 1)]
# print(dp)

dp[0][0][0] = 1

for i in range(n):
    for a in range(3):
        for b in range(3):
            cs = [sched_all[i]] if sched_all[i] != -1 else [0, 1, 2]
            for c in cs:
                if i >= 2 and a == b == c:
                    continue
                dp[i + 1][b][c] += dp[i][a][b]

res = 0
for i in range(3):
    for j in range(3):
        res += dp[n][i][j]

print(res % 10 ** 4)
