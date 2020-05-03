#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

N = int(input())
A = list(map(int, input().split()))

min_diff = 1
max_diff = N - 1

count = 0
for diff in range(min_diff, max_diff + 1):
    pairs = []
    i = 1
    while True:
        j = i + diff
        if j <= N:
            pairs.append([i, j])
        else:
            break
        i += 1
    # pprint(pairs)
    for i, j in pairs:
        if abs(i - j) == A[i-1] + A[j-1]:
            count += 1

print(count)
