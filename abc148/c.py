#!/usr/bin/env python

a, b = map(int, input().split())
# print(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# lcm(a, b) = a * b / gcd(a, b)
lcm = int(a * b / gcd(a, b))
print(lcm)
