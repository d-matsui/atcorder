#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


# 高さ h_limit を超えないように風船 i を割るには、何秒までに風船 i を割らなければ良いかを考える
# そのタイムリミットが小さいものから順に割るという戦略を取る
# 高さ h_limit を [h_min, h_max] の範囲で二分探索し、最適解を求める

N = int(input())
H = []
S = []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)


def bs(left, right):
    while left < right:
        h_limit = (left + right) // 2
        if can_crack(h_limit):
            right = h_limit
        else:
            left = h_limit + 1
    return left


def can_crack(h_limit):
    time_limit_list = [(h_limit - H[i]) / S[i] for i in range(N)]
    time = 0
    for time_limit in sorted(time_limit_list):
        if time > time_limit:
            return False
        time += 1
    return True


h_final_list = [H[i] + S[i] * (N - 1) for i in range(N)]
h_limit_min = min(h_final_list)
h_limit_max = max(h_final_list)
# print(h_final_list)
# print(h_limit_min, h_limit_max)

ans = bs(h_limit_min, h_limit_max)
print(ans)
