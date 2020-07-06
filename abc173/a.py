#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n = int(input())

res = n % 1000
if res == 0:
    print(0)
else:
    print(1000 - res)
