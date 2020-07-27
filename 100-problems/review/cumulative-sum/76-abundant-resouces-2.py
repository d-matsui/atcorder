#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
A = list(map(int, input().split()))

s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]
# print(s)

for k in range(1, N+1):
    max_sum = 0
    for i in range(k, N+1):
        max_sum = max(max_sum, s[i] - s[i-k])
    print(max_sum)
