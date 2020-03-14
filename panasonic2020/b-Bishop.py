#!/usr/bin/env python3

import math

H, W = map(int, input().split())

# ポイント: コーナーケースを避けるため、制約の下限に注意する。
# 今回だと、H == 1 or W == 1のとき、必ず1になってしまう。

if H == 1 or W == 1:
    print(1)
elif H % 2 == 1 and W % 2 == 1:
    print(math.ceil(H * W / 2))
else:
    print(int(H * W / 2))
