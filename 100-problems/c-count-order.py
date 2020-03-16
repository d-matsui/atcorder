#!/usr/bin/env python3

import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
# print(N, P, Q)

perms = list(map(list, itertools.permutations(range(1, N+1), N)))
perms.sort()
# print(perms)
# print(perms.index([1, 2, 3]))
# print(perms.index([3, 2, 1]))

a = perms.index(P) + 1
b = perms.index(Q) + 1

print(abs(a - b))
