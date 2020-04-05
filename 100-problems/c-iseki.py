#!/usr/bin/env python3

# 解法
# n個の点P = (p_1, ..., p_n)を辞書式順序でソートする。
# Pに含まれる任意の二点p_i, p_jに対して、線分p_i p_jを辺とする正方形のうち、
# p_iからp_jに進む向きが正方形を反時計回りにまわるものを考える。
# その正方形のp_i, p_jを除いた残りの二点q, rがPに含まれるかどうかを調べる(O(log_n))。
# 具体的には、
# q = (x_j - y_j + y_i, y_j + x_j - x_i)
# r = (x_i - y_j + y_i, y_i + x_j - x_i)
# であるから、このq, rがともにPに含まれるかどうかを調べる。
# このとき、この正方形の面積は、(x_i - x_j)^2 + (y_i - y_j)^2で求まる。
# Pの点からなる正方形を全て見つけ、その中から面積が最大であるものを求めればよい。
import itertools

n = int(input())
P = []
for i in range(n):
    l = list(map(int, input().split()))
    P.append(l)
# P = sorted(P)
# print(P)

combs = list(map(list, itertools.permutations(P, 2)))
# print(combs)

def is_square(points):
    combs = list(map(list, itertools.combinations(points, 2)))
    l = []
    # 任意の二点間の距離の二乗をそれぞれ求める
    for comb in combs:
        x1, y1 = comb[0][0], comb[0][1]
        x2, y2 = comb[1][0], comb[1][1]
        dist_square = pow(abs(x2 - x1), 2) + pow(abs(y2 - y1), 2)
        l.append(dist_square)
    # 各距離の二乗の比が1:1:1:1:2:2であれば正方形
    l_sorted = sorted(l)
    length = l_sorted[0]
    if l_sorted[1] == length and l_sorted[2] == length and l_sorted[3] == length and l_sorted[4] == length*2 and l_sorted[5] == length*2:
        return True
    return False

points = [[1,1], [4,3], [2,3], [-1,4]]
print(is_square(points))

# ----- 愚直な全探索 (NG) -----
# import itertools

# n = int(input())
# points_all = []
# for i in range(n):
#     l = list(map(int, input().split()))
#     points_all.append(l)
# print(n, points_all)


# def area(points):
#     return dist

# # list(itertools.combinations(points_all, 4))だと、
# # listのtupleのlistになってしまうことに注意
# l_points = list(map(list, itertools.combinations(points_all, 4)))
# l_area = []
# for points in l_points:
#     if is_square(points):
#         l_area = area(points)

# if len(l_area) == 0:
#     print(1)
# else:
#     print(min(l_area))
