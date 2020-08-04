#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
s = list(input())

num_w = 0
for i in range(N):
    if s[i] == 'W':
        num_w += 1
num_r = N - num_w
# print(num_w, num_r)

# [解法]
# 例えば N = 4, s = WWRR を考える
# 条件を見たす並べ方は、
# RRRR, RRRW, RRWW, RWWW, WWWW
# の N+1 通り存在する
# ここで、以下のような N+1 通りの区切り d を考える
# d: 0   1   2   3   4
# i: | 0 | 1 | 2 | 3 |
# s: | W | W | R | R |
# すると、達成したいことは
# d より左側にある W の数 num_w_before_d を 0 にして、
# d より右側にある R の数 num_r_after_d を 0 にすることである
# これを達成するには、少なくとも max(num_w_before_d, num_r_after_d) の手数がかかる
# 従って、N+1 通りの d に対して max(num_w_before_d, num_r_after_d) を計算し、
# それらの最小値を求めれば良い


def count_w_before_d(num_w_before_d, d):
    if d == 0:
        return 0
    if s[d-1] == 'W':
        num_w_before_d += 1
    return num_w_before_d


def count_r_after_d(num_r_after_d, d):
    if d == 0:
        return num_r
    if s[d-1] == 'R':
        num_r_after_d -= 1
    return num_r_after_d

ans = INF
num_w_before_d = 0
num_r_after_d = num_r
for d in range(N+1):
    num_w_before_d = count_w_before_d(num_w_before_d, d)
    num_r_after_d = count_r_after_d(num_r_after_d, d)
    ans = min(ans, max(num_w_before_d, num_r_after_d))

print(ans)
