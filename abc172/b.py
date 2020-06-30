#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


S = list(input())
T = list(input())

res = 0
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    res += 1

print(res)
