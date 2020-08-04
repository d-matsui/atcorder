#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


# if a[i] in c_dict:
  # s[i+1] = s[i]
# else:
  # s[i+1] = s[i] + 1

# 累積和でいけるかなと思ったがだめだ...
