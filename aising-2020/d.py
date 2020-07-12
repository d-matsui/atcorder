#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n = int(input())
x = input()
x_pc = x.count('1')
x_pc_plus = x_pc + 1
x_pc_minus = x_pc - 1

# 2 ** i % x_pc_plus, 2 ** i % x_pc_minus を予め計算しておく
r_plus_list = [pow(2, i, x_pc_plus) for i in range(n+1)]
r_minus_list = [0] * (n+1)
if x_pc_minus > 0:
    r_minus_list = [pow(2, i, x_pc_minus) for i in range(n+1)]

x = x[::-1]
r_plus = 0
r_minus = 0
for i in range(n):
    if x[i] == '1':
        r_plus += r_plus_list[i]
        r_minus += r_minus_list[i]

for i in range(n-1, -1, -1):
    if x[i] == '0':
        diff = (r_plus + r_plus_list[i]) % x_pc_plus
    elif x_pc_minus >= 1:
        diff = (r_minus - r_minus_list[i]) % x_pc_minus
    else:
        print(0)
        continue
    ans = 1
    while diff > 0:
        diff = diff % bin(diff).count('1')
        ans += 1
    print(ans)
