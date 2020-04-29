#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

H, W, K, V = map(int, input().split())
A = []
for _ in range(H):
    line = list(map(int, input().split()))
    A.append(line)


# s[i][j] := [0, i) × [0, j) の領域にある地価の総和
# s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + a[i][j]
s = [[0 for j in range(W + 1)] for i in range(H + 1)]

for i in range(H):
    for j in range(W):
        s[i+1][j+1] += s[i][j+1] + s[i+1][j] - s[i][j] + A[i][j]
# pprint(s)


def cost_build(li, lj, ri, rj):
    price_house = (ri - li) * (rj - lj) * K
    price_land = s[ri][rj] - s[ri][lj] - s[li][rj] + s[li][lj]
    return price_land + price_house


max_area = 0
for li in range(H):
    for lj in range(W):
        for ri in range(li + 1, H + 1):
            for rj in range(lj + 1, W + 1):
                # print(f"({li}, {lj}), ({ri}, {rj})")
                if cost_build(li, lj, ri, rj) <= V:
                    max_area = max(max_area, (ri - li) * (rj - lj))

print(max_area)
