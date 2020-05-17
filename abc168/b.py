#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')

k = int(input())
s = list(input())

if len(s) <= k:
    print(''.join(s))
else:
    res = ''.join(s[:k])
    res += '...'
    print(res)
