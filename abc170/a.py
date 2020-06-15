#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


numbers = list(map(int, input().split()))

for idx, num in enumerate(numbers):
    if num == 0:
        print(idx + 1)
