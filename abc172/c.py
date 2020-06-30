#!/usr/bin/env python3

from pprint import pprint
from bisect import bisect_right
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = [0] * (N+1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
sum_B = [0] * (M+1)
for i in range(M):
    sum_B[i+1] = sum_B[i] + B[i]
# print(sum_A, sum_B)

res = 0
for i in range(N+1):
    time_A = sum_A[i]
    rest = K - time_A
    if rest < 0:
        continue
    j = bisect_right(sum_B, rest) - 1
    res = max(res, i + j)
print(res)
