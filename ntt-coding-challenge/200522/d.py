#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


n_lots, lot_number = map(int, input().split())
input_numbers = list(map(int, input().split()))

cum_sum = [0] * (n_lots + 1)
for i in range(n_lots):
    cum_sum[i + 1] = cum_sum[i] + input_numbers[i]
# print(cum_sum)

for i in range(1, n_lots + 1):
    print(f'i = {i}')
    j = 1
    while j < n_lots + 1:
        print(f'j = {j}')
        j += i
