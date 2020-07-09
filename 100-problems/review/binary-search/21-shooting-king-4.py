#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
H, S = [], []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

# 高さ h_limit を超えないように各風船を割ることができるか
# 風船iをh_limitを超えないように割るには、H[i] + S[i] * t <= h_limit より、
# t <= (h_limit - H[i]) / S[i] であればよい
# これはO(N)で判定できる
# 最適なh_limitを二分探索すれば、NlogNで解ける

worst_case = [H[i] + S[i] * (N-1) for i in range(N)]
h_max = max(worst_case)
h_min = min(worst_case)


def can_crack(h_limit):
    l_sec = sorted([(h_limit - H[i]) // S[i] for i in range(N)])
    time = 0
    for sec in l_sec:
        if time > sec:
            return False
        time += 1
    return True


def bfs():
    left = h_min
    right = h_max
    while left < right:
        h_limit = (left + right) // 2
        if can_crack(h_limit):
            right = h_limit
        else:
            left = h_limit + 1
    return left


res = bfs()
print(res)
