#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


# r < g < b
r, g, b = map(int, input().split())
k = int(input())


def is_valid(r, g, b, comb):
    for c in comb:
        if c == 'r':
            r *= 2
        elif c == 'g':
            g *= 2
        else:
            b *= 2
    if r < g < b:
        return True
    return False


l = ['r', 'g', 'b']
flag = False
for i in range(k+1):
    if i == 0:
        if is_valid(r, g, b, []):
            flag = True

    combs = list(itertools.combinations_with_replacement(l, i))
    for comb in combs:
        if flag:
            break
        if is_valid(r, g, b, comb):
            flag = True

if flag:
    print('Yes')
else:
    print('No')
