#!/usr/bin/env python3

import itertools
import math

N = int(input())
towns = []
for i in range(N):
    l = list(map(int, input().split()))
    towns.append(l)
# print(N, towns)

paths = list(map(list, itertools.permutations(range(N), N)))
# print(paths)

dists = []
for path in paths:
    dist = 0
    for i, v in enumerate(path):
        town = towns[v]
        if i != N - 1:
            town_next = towns[path[i+1]]
            # print(i)
            # print(town)
            # print(town_next)
            x1, y1 = town[0], town[1]
            x2, y2 = town_next[0], town_next[1]
            dist += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    dists.append(dist)

# print(dists)
print(sum(dists)/len(dists))
