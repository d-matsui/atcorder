#!/usr/bin/env python3

m = int(input())

target = []
for i in range(m):
    l = list(map(int, input().split()))
    target.append(l)

n = int(input())
pic = []
for i in range(n):
    l = list(map(int, input().split()))
    pic.append(l)

# print(m, n)
# print(target)
# print(pic)

# 解法
# 星座の中から一点pを選ぶ
# pが写真の中のn個の星の一つqに一致するよう平行移動させる方法を全て(n通り)考える
# ある方法に対して、星座の全ての点を平行移動させたとき、それらの点が写真に含まれているか調べる
# 含まれていればその平行移動の量を出力する

p = target[0]
# print("p:", p)
for i_pic in range(n):
    q = pic[i_pic]
    x_move, y_move = q[0] - p[0], q[1] - p[1]
    # print("q:", q)
    # print(f"x_move: {x_move}, y_move: {y_move}")
    isSame = True
    for j_target in range(m):
        x = target[j_target][0] + x_move
        y = target[j_target][1] + y_move
        # print(f"x: {x}, y: {y}")
        if not [x, y] in pic:
            isSame = False
    if isSame:
        print(x_move, y_move)
        break

# ---- 最初考えていたこと
# - 探したい星座(凸多角形)を成す線分のリストtarget_linesを求める
# - picの任意の二つの星から成る全ての線分のリストlines_allを求める
# - target_linesに含まれる各線分と傾きが同じである線分をall_linesから取り出し、linesとする
# - linesの交点を全て求め、座標のリストpointsとする
# - pointsとtargetをそれぞれ辞書式順にソートする
# - 以下のa, bをそれぞれ求める
# tx, ty = target[0][0], target[0][1]
# px, py = points[0][0], points[0][1]
# とし、
# a = px - tx
# b = py - ty
