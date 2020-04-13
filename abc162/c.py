#!/usr/bin/env python3

import math
from functools import reduce

k = int(input())


def gcd(*numbers):
    return reduce(math.gcd, numbers)


res = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            res += gcd(a, b, c)

print(res)
