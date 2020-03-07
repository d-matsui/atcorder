#!/usr/bin/env python3

import itertools

n = int(input())
points_all = []
for i in range(n):
    l = list(map(int, input().split()))
    points_all.append(l)
print(n, points_all)

def is_square(points):
    combs = list(map(list, itertools.combinations(points, 2)))
    l = []
    # 任意の二点間の距離の二乗をそれぞれ求める
    for comb in combs:
        x1, y1 = comb[0][0], comb[0][1]
        x2, y2 = comb[1][0], comb[1][1]
        dist_square = pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2)
        l.append(dist_square)
    # 各距離の二乗の比が1:1:1:1:2:2であれば正方形
    l_sorted = sorted(l)
    length = l_sorted[0]
    if l_sorted[1] == length and l_sorted[2] == length and l_sorted[3] == length and l_sorted[4] == length*2 and l_sorted[5] == length*2:
        return True
    return False

def area(points):
    return 0

# list(itertools.combinations(points_all, 4))だと、
# listのtupleのlistになってしまうことに注意
l_points = list(map(list, itertools.combinations(points_all, 4)))
l_area = []
for points in l_points:
    if is_square(points):
        l_area = area(points)

if len(l_area) == 0:
    print(1)
else:
    print(min(l_area))
