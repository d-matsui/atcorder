#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, X, T = map(int, input().split())

q = N // X
r = N % X

if r == 0:
    print(q * T)
else:
    print(q * T + T)
