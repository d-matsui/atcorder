#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
inf = float("inf")


def is_multiple_2019(num):
    if num % 2019 == 0:
        return True
    return False


s = list(input())
len_s = len(s)

i = 0
count = 0
for j in range(len_s):
    if i < j:
        num = int(''.join(s[i:j+1]))
        if is_multiple_2019(num):
            count += 1
            i = j

print(count)
