#!/usr/bin/env python3

from bisect import bisect_left, bisect_right
from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_blocks = int(input())
blocks_top = sorted(list(map(int, input().split())))
blocks_middle = sorted(list(map(int, input().split())))
blocks_bottom = sorted(list(map(int, input().split())))
# pprint(blocks_top)
# pprint(blocks_middle)
# pprint(blocks_bottom)

res = 0
for middle in blocks_middle:
    index_top = bisect_left(blocks_top, middle)
    index_bottom = bisect_right(blocks_bottom, middle)
    # print(f"middle = {middle}")
    # print(f"index_top = {index_top}")
    # print(f"index_bottom = {index_bottom}\n")
    res += index_top * (n_blocks - index_bottom)

print(res)
