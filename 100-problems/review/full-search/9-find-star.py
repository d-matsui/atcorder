#!/usr/bin/env python3

# 1 <= m <= 200, 1 <= n <= 1000

m = int(input())

sign = []
for _ in range(m):
    x, y = map(int, input().split())
    sign.append([x, y])

n = int(input())
pic = []
for _ in range(n):
    x, y = map(int, input().split())
    pic.append([x, y])

# print(m, n)
# print(sign, pic)

# 星座中のある星に着目する
# その星と写真中の各星を一致させるのに必要な平行移動の仕方を求める
# n通りの平行移動の仕方に対して、星座が写真に含まれるかを判定する

star_sign = sign[0]
movements = []
for star in pic:
    x_move = star[0] - star_sign[0]
    y_move = star[1] - star_sign[1]
    movements.append([x_move, y_move])
# print(movements)


def exists(sign, pic):
    # print(f"sign: {sign}, pic: {pic}")
    for star in sign:
        if star not in pic:
            return False
    return True


def move(sign, x, y):
    sign_moved = [[sign[i][0] + x, sign[i][1] + y] for i in range(len(sign))]
    return sign_moved


for x_move, y_move in movements:
    sign_moved = move(sign, x_move, y_move)
    if exists(sign_moved, pic):
        print(x_move, y_move)
        break
