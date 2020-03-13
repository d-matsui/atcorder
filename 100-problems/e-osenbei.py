#!/usr/bin/env python3

import copy

R, C = map(int, input().split())
senbeis = []
for i in range(R):
    l = list(map(int, input().split()))
    senbeis.append(l)

# print(R, C)
# print(senbeis)

sums = []
for bits in range(2 ** R):
    # senbeis_rev = copy.deepcopy(senbeis)
    senbeis_rev = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            senbeis_rev[i][j] = senbeis[i][j]
    # print(bin(bits))
    # 各行の裏返し
    for row in range(R):
        if bits & (1 << row):
            for culumn in range(C):
                if senbeis[row][culumn] == 1:
                    senbeis_rev[row][culumn] = 0
                else:
                    senbeis_rev[row][culumn] = 1
    # print(f"revesed senbeis: {senbeis_rev}")
    sum = 0
    # 各列の裏返し
    for culumn in range(C):
        num_front = 0
        num_back = 0
        for row in range(R):
            if senbeis_rev[row][culumn] == 1:
                num_front += 1
            else:
                num_back += 1
        # print(f"num_front: {num_front}")
        # print(f"num_back: {num_back}")
        # 表向き煎餅の枚数の方が裏向き煎餅の枚数より大きいとき
        if  num_front > num_back:
            # print("culumn reverse")
            num_back = num_front
        sum += num_back
        # print(num_back)
    sums.append(sum)

# print(sums)
print(max(sums))

# ----- 方針 -----
# i行目を裏返すとき1が立つようなR個のbitを考える。
# e.g., bits: 000101
# bitsで1が立っている行を全て裏返したあとの、j列に存在する煎餅の表側の枚数と裏側の枚数を考える。
# その表側の枚数の方が、裏側の枚数より大きければj列を裏返すべきである。
# 上記のようにして、bitsで1が立っている行を全て裏返したあとj列を裏返したときの、出荷できる煎餅の枚数sumを求める。
# bit全探索したときの全てのsumを求め、その最大値を求める。
