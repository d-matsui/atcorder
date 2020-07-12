#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())


def g(x, y, z):
    return (x + y + z) ** 2 - (x*y + y*z + z*x)


xyz_dict = defaultdict(int)
num_dict = defaultdict(int)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            num = g(x, y, z)
            if (x, y, z) in xyz_dict:
                continue
            xyz_dict[(x, y, z)] = 1
            num_dict[num] += 1


for n in range(1, N+1):
    print(num_dict[n])
