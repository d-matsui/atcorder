#!/usr/bin/env python3

import itertools
import copy

k = int(input())
queens = []
for i in range(k):
    l = list(map(int, input().split()))
    queens.append(l)
# print(k, queens)

n = 8
column_rest = list(range(n))
row_ignore = []
for queen in queens:
    row_ignore.append(queen[0])
    column_rest.remove(queen[1])
# print(row_ignore)
# print(column_rest)

perms = list(map(list, itertools.permutations(column_rest, n-k)))
# print(perms)

def is_8queens(queens):
    for queen in queens:
        row, column = queen[0], queen[1]
        rest = [q for q in queens if q != queen]
        for i in range(len(queens)):
            up_left = [] if row == 0 or column == 0 else [row-i, column-i]
            up_right = [] if row == 0 or column == len(queens)-1 else [row-i, column+i]
            down_left = [] if row == len(queens)-1 or column == 0 else [row+i, column-i]
            down_right = [row+i, column+i] if row == len(queens)-1 or column == len(queens)-1 else []
            if up_left in rest or up_right in rest or down_left in rest or down_right in rest:
                return False
    return True

# 順列全探索
for perm in perms:
    # print(f"perm: {perm}")
    queens_copy = queens[:]
    index = 0
    # print(f"row_ignore: {row_ignore}")
    for i in range(n):
        if i not in row_ignore:
            queens_copy.append([i, perm[index]])
            index += 1
    queens_copy.sort()
    # print(f"queens_copy: {queens_copy}/n")
    if is_8queens(queens_copy):
        queens = queens_copy
        break

# initialize squares
squares = [["."] * n for i in range(n)]
for queen in queens:
    i = queen[0]
    j = queen[1]
    squares[i][j] = "Q"

# print squares
for i in range(n):
    for j in range(n):
        print(squares[i][j], end="")
    print("\n", end="")
