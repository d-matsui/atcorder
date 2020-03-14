#!/usr/bin/env python3

import math

H, W = map(int, input().split())

if H % 2 == 1 and W % 2 == 1:
    print(math.ceil(H * W / 2))
else:
    print(int(H * W / 2))
