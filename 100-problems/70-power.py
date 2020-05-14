#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

MOD = 1000000007
m, n = map(int, input().split())


def pow_fast(m, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_fast(m * m % MOD, n / 2)
    else:
        return pow_fast(m * m % MOD, int(n / 2)) * m % MOD


print(pow_fast(m, n))
