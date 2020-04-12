#!/usr/bin/env python3

import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
C = sorted(C)

res = 0
for b in B:
    index_a = bisect.bisect_left(A, b)
    index_c = bisect.bisect_right(C, b)
    res += index_a * (N - index_c)

print(res)
