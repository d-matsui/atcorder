#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

N, M, X = map(int, input().split())
C = []
for _ in range(N):
    line = list(map(int, input().split()))
    C.append(line)
# pprint(C)

res = INF
for i in range(2 ** N):
    books = []
    for j in range(N):
        if i & (1 << j):
            books.append(C[j])
    total = 0
    level = [0] * M
    for book in books:
        total += book[0]
        for idx, l in enumerate(book[1:]):
            level[idx] += l
    flag = True
    for lev in level:
        if lev < X:
            flag = False
    if flag:
        res = min(res, total)

if res == INF:
    print('-1')
else:
    print(res)
