#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys
import math

sys.setrecursionlimit(10 ** 6)

a, b, n = map(int, input().split())


def func(x):
    return math.floor(a * x / b) - a * math.floor(x / b)


def trisect(func):
    left = 0
    right = n
    while abs(right - left) > 0.001:
        d = right - left
        mid_left = left + d / 3
        mid_right = right - d / 3
        if func(mid_left) < func(mid_right):
            left = mid_left
        else:
            right = mid_right
    return left


x = trisect(func)
# print(x)
print(max(func(math.floor(x)), func(math.ceil(x)))
