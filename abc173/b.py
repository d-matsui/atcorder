#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n = int(input())
str_list = []
for _ in range(n):
    s = str(input())
    str_list.append(s)
# print(str_list)

res = [0] * 4

for s in str_list:
    if s == 'AC':
        res[0] += 1
    if s == 'WA':
        res[1] += 1
    if s == 'TLE':
        res[2] += 1
    if s == 'RE':
        res[3] += 1

print(f'AC x {res[0]}')
print(f'WA x {res[1]}')
print(f'TLE x {res[2]}')
print(f'RE x {res[3]}')
