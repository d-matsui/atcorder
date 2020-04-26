#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
inf = float("inf")

s, w = map(int, input().split())

if w >= s:
    print('unsafe')
else:
    print('safe')
