#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

x = int(input())
year = 0
money = 100
while True:
    year += 1
    money += money // 100
    if money >= x:
        break

print(year)
