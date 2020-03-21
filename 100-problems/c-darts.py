#!/usr/bin/env python3

# 1 <= N <= 1000
# 1 <= M <= 2 * 10 ** 8
# 1 <= P_i <= 10 ** 8

from bisect import bisect_right
# import itertools

N, M = map(int, input().split())
P = []
for _ in range(N):
    line = int(input())
    P.append(line)
# print(N, M, P)


def is_ok(array, index, value):
    if array[index] >= value:
        return True
    return False


def bs(array, value, is_ok):
    left = -1
    right = len(array)
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if is_ok(array, mid, value):
            right = mid
        else:
            left = mid
    return right


# 解法
# 4 本の矢を投げることを、
# まず 2 本の矢をまとめて投げて、次に 2 本の矢をまとめて投げる、として考える

P.append(0)
# combs = list(map(list, itertools.combinations_with_replacement(P, 2)))
# print(combs)
# Q = list(map(sum, combs))

# Q = []
Q = set()
for i in range(N + 1):
    for j in range(N + 1):
        Q.add(P[i] + P[j])
Q = sorted(list(Q))
# print(Q)

sum_max = -1
for q in Q:
    if q > M:
        break
    # Q_i + Q_j <= Mを満たすjのうち、最大のものを求める
    # Q_j <= M - Q_i
    j = bisect_right(Q, M - q)
    sum_max = max(sum_max, q + Q[j-1])

print(sum_max)
