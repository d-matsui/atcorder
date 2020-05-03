#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

n, k = map(int, input().split())

d = []
flags = [0 for i in range(n + 1)]

for i in range(k):
    d.append(int(input()))
    line = list(map(int, input().split()))
    for l in line:
        flags[l] += 1

count = 0
for i in range(1, n + 1):
    if flags[i] == 0:
        count += 1

print(count)
