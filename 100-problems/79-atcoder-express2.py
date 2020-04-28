#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

N, M, Q = map(int, input().split())
l_left = []
l_right = []
for _ in range(M):
    left, right = map(int, input().split())
    l_left.append(left)
    l_right.append(right)

l_query = []
for _ in range(Q):
    p, q = map(int, input().split())
    l_query.append([p, q])

# s[left][right] := (0, 0), (left, right) の領域に含まれる列車の数
# s[left][right] = s[left-1][right] + s[left][right-1] - s[left-1][right-1] + a[left][right]

s = [[0 for right in range(N + 1)] for left in range(N + 1)]

for i in range(M):
    left = l_left[i]
    right = l_right[i]
    s[left][right] += 1

for left in range(1, N + 1):
    for right in range(1, N + 1):
        s[left][right] += s[left-1][right] + s[left][right-1] - s[left-1][right-1]

# p <= left, right <= q であるようなleft, rightに対して、
# (left-1, left-1), (right, right) の領域に含まれる列車の数を求める

for left, right in l_query:
    res = s[right][right] - s[right][left-1] - s[left-1][right] + s[left-1][left-1]
    print(res)
