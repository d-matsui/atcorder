#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n_balloons = int(input())
H = []
S = []
for _ in range(n_balloons):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

penalties = [H[i] + S[i] * (n_balloons - 1) for i in range(n_balloons)]
# print(penalties)
min_penalty = min(penalties)
max_penalty = max(penalties)


def is_valid(penalty):
    limits = sorted([(penalty - H[i]) / S[i] for i in range(n_balloons)])
    time = 0
    for limit in limits:
        if time > limit:
            return False
        time += 1
    return True


def bs(left, right):
    # print(f'left = {left}, right = {right}')
    while left < right:
        mid = (left + right) // 2
        # print(f'mid = {mid}')
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return left


res = bs(min_penalty, max_penalty)
print(res)
