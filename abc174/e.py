#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


# K 回丸太を切った後、最も長い丸太の長さ x を L-1 < x <= L にできるか
# 上記のような L を二分探索で求める?
# x が決まらないのでダメでは
