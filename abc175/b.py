#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
L = list(map(int, input().split()))
# print(L)

# perms = itertools.permutations(L, 3)
# print(list(perms))

res = 0
for i in range(len(L)):
    for j in range(i+1, len(L)):
        for k in range(j+1, len(L)):
            if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
                # abs(a - b) < c < a + b
                if abs(L[i] - L[j]) < L[k] < L[i] + L[j]:
                    # print(i, j, k)
                    res += 1

# for a, b, c in perms:
#     if a != b and b != c:
#         if abs(a - b) < c < a + b:
#             res += 1

print(res)
