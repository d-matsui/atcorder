#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


n = int(input())
A = list(map(int, input().split()))

indices = [*range(n)]
sorted_indices = sorted(indices, key=lambda i: -A[i])
sorted_num = [A[i] for i in sorted_indices]
# print(sorted_indices)
# print(sorted_num)

res = []
for idx, i in enumerate(sorted_indices):
    num_i = A[i]
    # print(f'num_i = {num_i}')
    is_ok = True
    for j in range(idx + 1, n):
        num_j = sorted_num[j]
        # print(f'num_j = {num_j}')
        if num_i % num_j == 0:
            # print(f'False')
            is_ok = False
            break
    if idx == n - 1 and num_i == A[i-1]:
        is_ok = False
    if is_ok:
        res.append(i + 1)

print(len(res))
