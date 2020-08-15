#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)


S = input()

res = 0
if S == 'RSS' or S == 'SRS' or S == 'SSR' or S == 'RSR':
    res = 1
elif S == 'RRS' or S == 'SRR':
    res = 2
elif S == 'RRR':
    res = 3

print(res)
