#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import math
import itertools
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

N = int(input())
A = list(map(int, input().split()))

min_diff = 1
max_diff = N - 1

dl = defaultdict(list)
dr = defaultdict(list)
for i in range(1, N + 1):
    key = i + A[i-1]
    dl[key].append(i)
    key = i - A[i-1]
    if key > 0:
        dr[key].append(i)
# pprint(dict(dl))
# pprint(dict(dr))

count = 0
for diff in range(min_diff, max_diff + 1):
    count += len(dl[diff]) * len(dr[diff])
print(count)
