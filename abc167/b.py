#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

a, b, c, k = map(int, input().split())

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    rest = k - (a + b)
    print(a - rest)
