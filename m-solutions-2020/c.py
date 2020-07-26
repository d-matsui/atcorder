#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, K = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]
# pprint(s)

prev = s[K]
for i in range(K+1, N+1):
    # print(f'i = {i}')
    # print(f's[i] = {s[i]}, s[i-K] = {s[i-K]}')
    score = s[i] - s[i-K]
    # print(f'score = {score}')
    if prev < score:
        print('Yes')
    else:
        print('No')
    prev = score
