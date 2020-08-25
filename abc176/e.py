#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


H, W, M = map(int, input().split())

num_boms_row = [0] * H
max_boms_row = [None, 0]

num_boms_col = [0] * W
max_boms_col = [None, 0]

boms = set()

for _ in range(M):
    h, w = map(int, input().split())
    # 0-index
    h -= 1
    w -= 1

    boms.add((h, w))
    num_boms_row[h] += 1
    num_boms_col[w] += 1

    if max_boms_row[1] < num_boms_row[h]:
        max_boms_row = [h, num_boms_row[h]]

    if max_boms_col[1] < num_boms_col[w]:
        max_boms_col = [w, num_boms_col[w]]

# pprint(max_boms_row)
# pprint(max_boms_col)

ans = max_boms_row[1] + max_boms_col[1]
if (max_boms_row[0], max_boms_col[0]) in boms:
    ans -= 1
print(ans)
