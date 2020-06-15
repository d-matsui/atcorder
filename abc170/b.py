#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


x, y = map(int, input().split())

if y % 2 == 1:
    print('No')
else:
    if x * 2 <= y <= x * 4:
        print('Yes')
    else:
        print('No')
