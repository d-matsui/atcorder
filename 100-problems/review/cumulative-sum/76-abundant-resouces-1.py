#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
A = list(map(int, input().split()))

cum_sum = [0] * (N+1)
for i in range(N):
    cum_sum[i+1] = cum_sum[i] + A[i]
# print(cum_sum)


for k in range(1, N+1):
    max_sum = 0
    for left in range(N):
        right = left + k
        if right <= N:
            max_sum = max(max_sum, cum_sum[right] - cum_sum[left])
    print(max_sum)
