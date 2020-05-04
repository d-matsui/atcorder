#!/usr/bin/env python3

import sys

input = sys.stdin.buffer.readline

x = int(input())


def find(x):
    for a in range(-300, 300):
        for b in range(-300, 300):
            if a ** 5 - b ** 5 == x:
                return [a, b]


a, b = find(x)
print(a, b)
