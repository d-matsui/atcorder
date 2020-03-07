#!/usr/bin/env python3

A, B = map(int, input().split())

price = "-1"
for x in range(1, 100000+1):
    if int(x * 0.08) == A and int(x * 0.1) == B:
        price = x
        break

print(price)
