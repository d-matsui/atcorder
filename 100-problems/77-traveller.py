#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")
divisor = 10 ** 5

n_towns, m_days = map(int, input().split())

dists = []
for _ in range(n_towns - 1):
    d = int(input())
    dists.append(d)

moves = []
for _ in range(m_days):
    move = int(input())
    moves.append(move)
# print(dists, moves)

cum_sum = [0 for _ in range(n_towns)]
for i in range(n_towns - 1):
    cum_sum[i + 1] = cum_sum[i] + dists[i]
# print(cum_sum)

total = 0
start = 0
for move in moves:
    goal = start + move
    # print(f"start = {start}, goal = {goal}")
    if move > 0:
        d = cum_sum[goal] - cum_sum[start]
    else:
        d = cum_sum[start] - cum_sum[goal]
    # print(f"d = {d}")
    total += d
    start = goal

print(total % divisor)
