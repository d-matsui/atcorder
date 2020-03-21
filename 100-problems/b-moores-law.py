#!/usr/bin/env python3

p = float(input())


def f(x):
    return x + p / 2 ** (x / 1.5)


def f_prime(x):
    return 1 - 0.462098 * (2 ** (-0.666667 * x)) * p


def bs(func, value):
    left = 0.0
    right = 100.0
    while abs(right - left) > 0.0000000001:
        mid = (left + right) / 2
        # print(f"left: {left}, right: {right}, mid: {mid}")
        if func(left) < 0 and func(mid) < 0:
            left = mid
        elif func(right) > 0 and func(mid) > 0:
            right = mid
    return mid


def trisect_minimul(func):
    left = 0
    right = 100
    while abs(right - left) > 0.000000001:
        d = right - left
        x1 = left + d/3
        x2 = right - d/3
        # print(f"d, x1, x2: {d}, {x1}, {x2}")
        if func(x1) < func(x2):
            right = x2
        elif func(x1) > func(x2):
            left = x1
        else:
            return left
    return left


x = trisect_minimul(f)
print(x)
print(f(x))

# x = bs(f_prime, 0)
# # print(x)
# print(f(x))
