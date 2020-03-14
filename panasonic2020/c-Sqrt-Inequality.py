#!/usr/bin/env python3

import math

a, b, c = map(int, input().split())

# if math.sqrt(a) + math.sqrt(b) < math.sqrt(c):
#     print("Yes")
# else:
#     print("No")

if a + b - c + (2 * math.sqrt(a * b)) < 0:
    print("Yes")
else:
    print("No")
