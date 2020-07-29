#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n, q = map(int, input().split())

queries = []
for _ in range(q):
    com, x, y = map(int, input().split())
    queries.append([com, x, y])

parents = [i for i in range(n)]


def root(x):
    if x == parents[x]:
        return x
    parents[x] = root(parents[x])
    return parents[x]


def same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x_root = root(x)
    y_root = root(y)
    if x_root != y_root:
        parents[x_root] = y_root


for com, x, y in queries:
    if com == 0:
        unite(x, y)
    else:
        if same(x, y):
            print('1')
        else:
            print('0')
