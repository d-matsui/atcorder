#!/usr/bin/env python3

x, y, z = map(int, input().split())

tmp1 = x
x = y
y = tmp1

tmp2 = x
x = z
z = tmp2

print(x, y, z)
