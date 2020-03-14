#!/usr/bin/env python3

import math

a, b, c = map(int, input().split())

# ポイント: 誤差を回避するため、整数で計算する
# sqrt(a) + sqrt(b) < sqrt(c)
# \equiv 2 * sqrt(a * b) < c - a - b (and c - a - b > 0)
# \equiv 4 * a * b < (c - a - b)^2 (and c - a - b > 0)

if 4 * a * b < (c - a - b) ** 2 and c - a - b > 0:
    print("Yes")
else:
    print("No")
