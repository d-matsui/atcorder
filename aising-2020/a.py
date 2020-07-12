#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


L, R, d = map(int, input().split())

res = 0
for i in range(L, R+1):
    if i % d == 0:
        res += 1
print(res)
