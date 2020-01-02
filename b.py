#!/usr/bin/env python3

a, b, k = map(int, input().split())
# print(a, b, k)

if k >= a + b:
    a = 0
    b = 0
else:
    if k >= a:
        b = b - (k - a)
        a = 0
        # print("k >= a")
        # print(a, b)
    else:
        # print("k < a")
        a = a - k
        b = b
        # print(a, b)

print(a, b)
