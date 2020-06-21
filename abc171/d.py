#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys
import bisect

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


N = int(input())
A = list(map(int, input().split()))

dict_A = defaultdict(int)
for a in A:
    dict_A[a] += 1

Q = int(input())
query = []
for _ in range(Q):
    b, c = map(int, input().split())
    query.append([b, c])

current_sum = sum(A)

for b, c in query:
    if b in dict_A:
        diff = c * dict_A[b] - b * dict_A[b]
        current_sum += diff
        dict_A[c] += dict_A[b]
        dict_A[b] = 0
    print(current_sum)
