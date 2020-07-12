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
A = [None] + A
# print(A)

res = 0
for i in range(1, N+1):
    if i % 2 == 1 and A[i] % 2 == 1:
        res += 1
print(res)
