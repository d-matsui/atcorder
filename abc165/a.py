#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

k = int(input())
a, b = map(int, input().split())

res = 0
flag = False
while res <= b:
    res += k
    if a <= res <= b:
        flag = True

if flag:
    print("OK")
else:
    print("NG")
