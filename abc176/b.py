#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


nums = list(map(int, (list(input()))))
# print(nums)

if sum(nums) % 9 == 0:
    print('Yes')
else:
    print('No')
