#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

n, m, q = map(int, input().split())
queries = []
for i in range(q):
    line = list(map(int, input().split()))
    queries.append(line)

numbers = range(1, m + 1)

combs = itertools.combinations_with_replacement(numbers, n)
# print(list(combs))

res_max = 0
for A in combs:
    res = 0
    for a, b, c, d in queries:
        if A[b-1] - A[a-1] == c:
            res += d
    res_max = max(res_max, res)

print(res_max)
