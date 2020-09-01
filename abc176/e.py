#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


H, W, M = map(int, input().split())

num_bombs_each_row = [0] * H
num_bombs_each_col = [0] * W
bombs = set()

for _ in range(M):
    h, w = map(int, input().split())
    # 0-index
    h -= 1
    w -= 1

    bombs.add((h, w))
    num_bombs_each_row[h] += 1
    num_bombs_each_col[w] += 1

max_bombs_in_row = max(num_bombs_each_row)
max_bombs_in_col = max(num_bombs_each_col)

rows_with_max_bombs = []
for row in range(H):
    if num_bombs_each_row[row] == max_bombs_in_row:
        rows_with_max_bombs.append(row)

cols_with_max_bombs = []
for col in range(W):
    if num_bombs_each_col[col] == max_bombs_in_col:
        cols_with_max_bombs.append(col)

found = False
for row in rows_with_max_bombs:
    for col in cols_with_max_bombs:
        if (row, col) not in bombs:
            found = True
            break

ans = max_bombs_in_row + max_bombs_in_col
if found:
    print(ans)
else:
    print(ans - 1)
