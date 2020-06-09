#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')

n_columns = int(input())
m_rows = 5

squares = []
for _ in range(m_rows):
    line = list(input())
    squares.append(line)
# pprint(squares)

# dp[i][j] := i列目目を色jで塗り潰したときの、1列目からi列目までに塗り替えた数の最小値
# dp[i][j] = min(dp[i-1][k] + 5 - (i列目のjの数))
# ここで、k \in {R, B, W}, k != jである。


def count_color(color_num, column):
    colors_dict = {0: 'R', 1: 'B', 2: 'W'}
    color = colors_dict[color_num]
    column -= 1
    count = 0
    for row in squares:
        if row[column] == color:
            count += 1
    return count


dp = [[INF for j in range(3)] for i in range(n_columns + 1)]

for color_num in range(3):
    dp[1][color_num] = m_rows - count_color(color_num, 1)

# pprint(dp)

for i in range(1, n_columns + 1):
    for j in range(3):
        count = count_color(j, i)
        for k in range(3):
            if k == j:
                continue
            dp[i][j] = min(dp[i][j], dp[i-1][k] + m_rows - count)

print(min(dp[n_columns]))
