#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7

N, Q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))


def fast_power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_power(x * x % MOD, n // 2)
    return fast_power(x * x % MOD, n // 2) * x % MOD


cum_sum = [0] * N
for i in range(1, N):
    cum_sum[i] = cum_sum[i-1] + fast_power(a[i-1], a[i])
# pprint(cum_sum)

res = 0
s = 1
for i, t in enumerate(c):
    res += abs(cum_sum[s-1] - cum_sum[t-1])
    if i == len(c) - 1:
        # print(f't = {t}, s = {s}')
        res += cum_sum[t-1] - cum_sum[1-1]
    s = t

print(res % MOD)
