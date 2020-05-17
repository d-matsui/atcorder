#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

len_hour_hand, len_minute_hand, hour, minute = map(int, input().split())

d_short = hour / 12 + (minute / 60) / 12
d_long = minute / 60
# print(f'd_long = {d_long}, d_short: {d_short}')

degrees = 360 * abs(d_long - d_short)
degrees = min(degrees, 360 - degrees)
radians = math.radians(degrees)

res = len_minute_hand ** 2 + len_hour_hand ** 2 - 2 * len_minute_hand * len_hour_hand * math.cos(radians)
print(math.sqrt(res))
