#!/usr/bin/env python3

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])


def bs(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1


def is_valid(points, p_i, p_j):
    x_i, y_i = p_i[0], p_i[1]
    x_j, y_j = p_j[0], p_j[1]
    x_q, y_q = x_j - (y_j - y_i), y_j + (x_j - x_i)
    x_r, y_r = x_i - (y_j - y_i), y_i + (x_j - x_i)
    if bs(points, [x_q, y_q]) == -1:
        return False
    if bs(points, [x_r, y_r]) == -1:
        return False
    return True


# 点集合をソートする
# 点集合から任意の二点p_i, p_jを選ぶ
# 線分p_i, p_jを辺とする正方形のうち、p_iからp_jへ進む方向が反時計周りであるような正方形を考える
# その正方形におけるp_i, p_jを除いた残りの二点をq, rとする
# q, rが点集合に存在するかを二分探索する


points = sorted(points)
max_area = 0

for i in range(n):
    for j in range(n):
        if i < j:
            p_i, p_j = points[i], points[j]
            if is_valid(points, p_i, p_j):
                x_i, y_i = p_i[0], p_i[1]
                x_j, y_j = p_j[0], p_j[1]
                area = (x_i - x_j) ** 2 + (y_i - y_j) ** 2
                max_area = max(max_area, area)

print(max_area)
