#!/usr/bin/env python3

from pprint import pprint
from bisect import bisect_left
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())

str_list = [chr(ord('a') + i) for i in range(26)]

exp_26 = [26 ** i for i in range(1, 12)]
# print(exp_26)
int_list = [26]
for i in range(10):
    n = int_list[i] + exp_26[i+1]
    int_list.append(n)
print(int_list)

num_str = bisect_left(int_list, N) + 1
print(f'num_str = {num_str}')

k = N if num_str == 1 else N - int_list[num_str-2]
print(f'k = {k}')

q, r = divmod(N, 26)
print(f'q = {q}, r = {r}')

if num_str == 1:
    res = str_list[r-1]
else:
    res = ''
    q %= 26
    print(f'q = {q}')
    for i in range(num_str-1):
        if r == 0:
            res += str_list[q-2]
        else:
            res += str_list[q-1]
    res += str_list[r-1]
print(res)
