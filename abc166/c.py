#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

N, M = map(int, input().split())
H = list(map(int, input().split()))
paths = []
for _ in range(M):
    line = list(map(int, input().split()))
    paths.append(line)

# print(H, path)

flags = [0 for _ in range(N)]
path = [[] for _ in range(N)]
for a, b in paths:
    path[a-1].append(H[b-1])
    path[b-1].append(H[a-1])

# print(path)

for i in range(N):
    if len(path[i]) == 0:
        flags[i] = 1
    else:
        if max(path[i]) < H[i]:
            flags[i] = 1

print(sum(flags))
