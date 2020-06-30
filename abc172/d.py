#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())

# 正の整数iに対して、iの倍数でありN以下であるものの総和をg(i)とおくと、
# 求めたい\sum_{K=1}^{N} K * f(K)は、
# \sum_{K=1}^{N} K * f(K) = \sum_{K=1}^{N} g(K)
# で与えられる。
# ここで、kをN/i以下の最大の整数とおくと、g(i)は、
# g(i) = i + 2 * i + 3 * i + ... + k * i = (1 + 2 + 3 + ... + k) * i
# = k * (k + 1) * i / 2 (等差数列の和)
# で与えられる。


def g(i):
    k = N // i
    return k * (k + 1) * i // 2


res = 0
for i in range(1, N+1):
    res += g(i)
print(res)
