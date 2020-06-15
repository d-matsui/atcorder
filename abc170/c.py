#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


x, n = map(int, input().split())
P = list(map(int, input().split()))

diff = INF
res = None

for i in range(-200, 200):
    if i in P:
        continue
    if abs(x - i) < diff:
        res = i
        diff = abs(x - i)

print(res)
