#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

a, b = map(int, input().split())

res = 1 / ((1 / a) + (1 / b))

print(int(res))
