#!/usr/bin/env python3

from pprint import pprint
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
orders = list(input())

x, y = 0, 0
direction = 'U'
battery = 10 ** 6

forward_x = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
forward_y = {'U': 1, 'R': 0, 'D': -1, 'L': 0}
rot_R = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}
rot_L = {'U': 'L', 'R': 'U', 'D': 'R', 'L': 'D'}

i = 0
while i < n:
    repeat = 1
    if orders[i].isdecimal():
        repeat = int(orders[i])
        i += 1
    for _ in range(repeat):
        if battery == 0:
            break
        if orders[i] == 'F':
            x += forward_x[direction]
            y += forward_y[direction]
        elif orders[i] == 'B':
            x -= forward_x[direction]
            y -= forward_y[direction]
        elif orders[i] == 'R':
            direction = rot_R[direction]
        else:
            # L
            direction = rot_L[direction]
        battery -= 1
    i += 1

print(x, y)
