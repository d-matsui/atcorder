#!/usr/bin/env python3

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
set_points = set(points)

max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        p_i, p_j = points[i], points[j]
        x_i, y_i = p_i[0], p_i[1]
        x_j, y_j = p_j[0], p_j[1]
        x_q, y_q = x_j - (y_j - y_i), y_j + (x_j - x_i)
        x_r, y_r = x_i - (y_j - y_i), y_i + (x_j - x_i)
        if (x_q, y_q) in set_points and (x_r, y_r) in set_points:
            area = (x_i - x_j) ** 2 + (y_i - y_j) ** 2
            max_area = max(max_area, area)

print(max_area)
