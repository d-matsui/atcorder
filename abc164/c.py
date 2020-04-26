#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
inf = float("inf")

n = int(input())
s = defaultdict(str)
for _ in range(n):
    key = input()
    s[key] = 1

print(len(dict(s)))
