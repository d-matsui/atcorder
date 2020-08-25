#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
A = list(map(int, input().split()))

ans = 0
prev = None
for a in A:
    if prev is None:
        prev = a
        continue
    if prev > a:
        diff = prev - a
    else:
        diff = 0
    ans += diff
    prev = a + diff

print(ans)
