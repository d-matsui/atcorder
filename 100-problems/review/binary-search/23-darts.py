#!/usr/bin/env python3

import bisect

n_targets, max_points = map(int, input().split())

points = [0]
for i in range(n_targets):
    points.append(int(input()))

# print(n_targets, max_points, points)

# 投げない状態を P_0 = 0 とする。
# 4 本の矢を投げることを、2 本の矢をまとめて投げるのを 2 回行うことと考える。
# 2 本の矢を投げたときに得られる点数の合計値を全通り ((N + 1)^2 通り) 求める。
# 最初の 2 本の矢を投げたときに得られる点数の合計が Q_i であったとする。
# 残りの 2 本の矢を投げたときに得られる点数の最大値を求めるには、
# Q_i + Q_j <= M を満たす j のうち、Q_j が最大となる j を求めればよい。

Q = set()
for i in range(n_targets + 1):
    for j in range(n_targets + 1):
        Q.add(points[i] + points[j])
Q = sorted(list(Q))
# print(Q)

res = 0
# print(f"max_points = {max_points}, Q = {Q}, len(Q) = {len(Q)}")
for q_i in Q:
    if q_i > max_points:
        continue
    j = bisect.bisect_right(Q, max_points - q_i) - 1
    q_j = Q[j]
    # print(f"q_i = {q_i}, q_j = {q_j}\n")
    res = max(res, q_i + q_j)

print(res)
