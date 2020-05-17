#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')

n = list(input())
n1 = int(n[-1])

if n1 == 2 or n1 == 4 or n1 == 5 or n1 == 7 or n1 == 9:
    print('hon')
elif n1 == 0 or n1 == 1 or n1 == 6 or n1 == 8:
    print('pon')
else:
    print('bon')
