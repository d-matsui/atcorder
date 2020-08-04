#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, D = map(int, input().split())

ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    if math.sqrt(x ** 2 + y ** 2) <= D:
        ans += 1

print(ans)
