#!/usr/bin/env python3

# 1 <= R <= 10, 1 <= C <= 10000
R, C = map(int, input().split())
crackers = []
for _ in range(R):
    line = list(map(int, input().split()))
    crackers.append(line)
# print(R, C, crackers)


def reverse_row(crackers_row):
    for col in range(C):
        if crackers_row[col] == 0:
            crackers_row[col] = 1
        else:
            crackers_row[col] = 0
    return crackers_row


def sum_col(crackers):
    sum_col = [0 for _ in range(C)]
    for row in range(R):
        for col in range(C):
            sum_col[col] += crackers[row][col]
    return sum_col


def calc(row):
    res = 0
    for x in row:
        res += max(x, R - x)
    return res


def copy(crackers):
    crackers_copy = [[0 for col in range(C)] for row in range(R)]
    for row in range(R):
        for col in range(C):
            crackers_copy[row][col] = crackers[row][col]
    return crackers_copy


max_res = 0
for i in range(2 ** R):
    # print(f"{bin(i)}")
    res = 0
    crackers_copy = copy(crackers)
    for row in range(R):
        if i & (1 << row):
            crackers_copy[row] = reverse_row(crackers_copy[row])
    s_col = sum_col(crackers_copy)
    # print(f"s_col: {s_col}")
    res = calc(s_col)
    max_res = max(max_res, res)

print(max_res)
