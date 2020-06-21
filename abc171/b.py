#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, K = map(int, input().split())
P = list(map(int, input().split()))
P = sorted(P)

res = 0
for i in range(K):
    res += P[i]
print(res)
