#!/usr/bin/env python3

from pprint import pprint
import sys
sys.setrecursionlimit(10 ** 6)

n_towns, k_times = map(int, input().split())
teleport = list(map(int, input().split()))

seq = []
flags = [False] * n_towns
visited = [0] * n_towns

flags[0] = True
seq.append(0)
visited[0] += 1

town_prev = 0

while True:
    town_next = teleport[town_prev] - 1
    visited[town_next] += 1
    if flags[town_next]:
        seq.append(town_next)
        break
    seq.append(town_next)
    flags[town_next] = True
    town_prev = town_next

loop_len = 0
for town, count in enumerate(visited):
    if count == 2:
        loop_idx = seq.index(town)
# print(loop_idx)

# print(f'seq: {seq}')

if k_times < loop_idx:
    print(seq[k_times] + 1)
else:
    arr = seq[loop_idx:len(seq) - 1]
    r = (k_times - loop_idx) % len(arr)
    print(arr[r] + 1)
