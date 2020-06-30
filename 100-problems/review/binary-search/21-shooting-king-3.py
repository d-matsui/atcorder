#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n = int(input())
H = []
S = []
for _ in range(n):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

# 高さ h_limit を超えないように全ての風船を割ることができるか、を考える。
# この h_limit の最小値を 0 < h_limit < 10 ** 9 の区間で二分探索することで求めたい。
# 高さ h_limit を超えないようにある風船を割るためには、
# h + s * time <= h_limit より、
# time <= (h_limit - h) / s を満たす必要がある。


def is_valid(h_limit):
    l_sec = sorted([(h_limit - H[i]) // S[i] for i in range(n)])
    time = 0
    for sec in l_sec:
        if time > sec:
            return False
        time += 1
    return True


def bs(left, right):
    while left < right:
        h_limit = (left + right) // 2
        if is_valid(h_limit):
            right = h_limit
        else:
            left = h_limit + 1
    return left


l_limit = [H[i] + S[i] * (n - 1) for i in range(n)]
res = bs(min(l_limit), max(l_limit))
print(res)
