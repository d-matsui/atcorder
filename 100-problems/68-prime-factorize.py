#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


def prime_factor(n):
    res = []
    dividend = n
    divisor = 2
    while divisor ** 2 <= n:
        while dividend % divisor == 0:
            dividend //= divisor
            res.append(divisor)
        divisor += 1
    if dividend != 1:
        res.append(dividend)
    return res


n = int(input())
res = prime_factor(n)
res_str = list(map(str, res))
print(f"{n}: {' '.join(res_str)}")
