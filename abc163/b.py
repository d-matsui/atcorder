#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
a = []
a = list(map(int, input().split()))

if sum(a) > n:
    print('-1')
else:
    print(n - sum(a))
