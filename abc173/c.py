#!/usr/bin/env python3

from pprint import pprint
import copy
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


H, W, K = map(int, input().split())
field = []
for _ in range(H):
    line = list(input())
    field.append(line)
# pprint(field)


def calc(field_copy):
    res = 0
    for i in range(H):
        for j in range(W):
            if field_copy[i][j] == '#':
                res += 1
    return res


res = 0
for row in range(2 ** H):
    for col in range(2 ** W):
        field_copy = copy.deepcopy(field)
        for i_row in range(H):
            if row & (1 << i_row):
                for j_col in range(W):
                    field_copy[i_row][j_col] = '_'
        for i_col in range(W):
            if col & (1 << i_col):
                for j_row in range(H):
                    field_copy[j_row][i_col] = '_'
        if calc(field_copy) == K:
            res += 1

print(res)
