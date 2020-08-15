#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


x, k, d = map(int, input().split())
x = abs(x)

ans = None
if x > d:
    q, r = divmod(x, d)
    if k <= q:
        ans = x - k * d
    else:
        y = x - q * d
        if (k - q) % 2 == 0:
            ans = y
        else:
            ans = min(abs(y + d), abs(y - d))
else:
    if k % 2 == 0:
        ans = x
    else:
        ans = abs(x - d)

print(ans)
