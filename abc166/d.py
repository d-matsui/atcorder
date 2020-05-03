#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

x = int(input())


def find(x):
    for a in range(10 ** 4):
        for b in range(10 ** 4):
            b = -b
            if a ** 5 - b ** 5 == x:
                return [a, b]


a, b = find(x)
print(a, b)
