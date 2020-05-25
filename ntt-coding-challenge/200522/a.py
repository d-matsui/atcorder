#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

price = int(input())

if price < 30000:
    print(0)
elif price < 100000:
    print(1)
elif price < 200000:
    print(2)
else:
    print(3)
