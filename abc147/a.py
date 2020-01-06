#!/usr/bin/env python3

a, b, c = map(int, input().split())

if a + b + c >= 22:
    print('bust')
elif a + b + c <= 21:
    print('win')
