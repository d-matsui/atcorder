#!/usr/bin/env python3

P = float(input())
# print(P)


def f(x):
    return x + P / 2 ** (x / 1.5)


def calc():
    eps = 10 ** (-8)
    left = 0
    right = 100
    while abs(left - right) > eps:
        d = right - left
        left_mid = left + (d / 3)
        right_mid = right - (d / 3)
        if f(left_mid) > f(right_mid):
            left = left_mid
        elif f(left_mid) < f(right_mid):
            right = right_mid
        else:
            return left
    return left


x = calc()
print(f(x))
