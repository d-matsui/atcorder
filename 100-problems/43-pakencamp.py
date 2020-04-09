#!/usr/bin/env python3

# 1 <= N <= 999
# S_{i, j} = R, B, W, #

n = int(input())

s = []
for _ in range(5):
    line = list(input())
    s.append(line)
# print(n, s)


def get_colors_excluded(col):
    colors = ['B', 'W', 'R']
    colors.remove(col)
    return colors


def get_color_num(col):
    if col == 'B':
        return 0
    elif col == 'W':
        return 1
    else:
        return 2


def cost_fill(column, color):
    cost = 0
    for row in range(5):
        if s[row][column] != color:
            cost += 1
    return cost


# dp[column][color]: column列までを考えたとき、column列が全てcolor色であるときの塗り替える回数の最小値
# dp[column][color] = min(dp[column][color], dp[colmun - 1][color_k] + column列をcolで塗った数)
# 0 <= column < 5, color = 0, 1, 2, color_k = [0, 1, 2].remove(color)

inf = float("inf")
dp = [[inf for color in range(3)] for column in range(n)]

for color in ['B', 'W', 'R']:
    color_num = get_color_num(color)
    dp[0][color_num] = cost_fill(0, color)

for column in range(1, n):
    for color in ['B', 'W', 'R']:
        color_num = get_color_num(color)
        colors = get_colors_excluded(color)
        for color_k in colors:
            color_k_num = get_color_num(color_k)
            dp[column][color_num] = min(dp[column][color_num], dp[column - 1][color_k_num] + cost_fill(column, color))

print(min(dp[n - 1]))
