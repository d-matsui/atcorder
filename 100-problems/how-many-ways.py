#!/usr/bin/env python3

import itertools

while True:
    count = 0
    n, x = map(int, input().split())
    # print(n, x)
    if n == 0 and x == 0:
        break
    l = range(1, n+1)
    combs = itertools.combinations(l, 3)
    count = 0
    for c in combs:
        if sum(c) == x:
            count += 1
    print(count)
