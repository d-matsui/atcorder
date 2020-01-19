#!/usr/bin/env python3

N = int(input())
P = list(map(int, input().split()))
# print(N, P)

count = 0
min_prev = P[0] + 1
for i in range(N):
    if P[i] < min_prev:
        min_prev = P[i]
        count += 1

print(count)
