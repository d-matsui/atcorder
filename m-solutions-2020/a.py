#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


rating = int(input())

if 400 <= rating <= 599:
    ans = 8
elif 600 <= rating <= 799:
    ans = 7
elif 800 <= rating <= 999:
    ans = 6
elif 1000 <= rating <= 1199:
    ans = 5
elif 1200 <= rating <= 1399:
    ans = 4
elif 1400 <= rating <= 1599:
    ans = 3
elif 1600 <= rating <= 1799:
    ans = 2
elif 1800 <= rating <= 1999:
    ans = 1

print(ans)
