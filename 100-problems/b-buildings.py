#!/usr/bin/env python3

N, K = map(int, input().split())
l_height = list(map(int, input().split()))
# print(N, K)
# print(l_height)

costs = []
if N == K:
    cost = 0
    max_height = l_height[0]
    for i in range(1, N):
        if max_height >= l_height[i]:
            cost += (max_height + 1) - l_height[i]
            l_height[i] = max_height + 1
        max_height = l_height[i]
    costs.append(cost)
else:
    for bits in range(2 ** N):
        buildings = []
        # bit立っている建物の番号のリストを求める
        for i in range(N):
            if bits & (1 << i):
                buildings.append(i)

        l_height_copy = l_height[:]
        cost = 0
        # K色の色を見えるようにしたときのcostを求める
        if len(buildings) == K:
            print(f"\nbits: {bin(bits)}")
            print(f"buildings: {buildings}")
            max_height = l_height_copy[0]
            for i in range(1, N):
                if l_height_copy[i] > max_height:
                    print(f"updated max_height: {max_height}")
                    max_height = l_height_copy[i]
                if i in buildings:
                    print(f"i: {i} is in buildings")
                    print(f"buildings: {buildings}")
                    print(f"l_height_copy: {l_height_copy}")
                    print(f"max_height: {max_height}")
                    print(f"l_height_copy[i]: {l_height_copy[i]}")
                    # 建物iの高さを増やす必要があるとき
                    if max_height >= l_height_copy[i]:
                        print("max_height >= l_height[i]")
                        print(f"diff: {(max_height + 1) - l_height_copy[i]}")
                        cost += (max_height + 1) - l_height_copy[i]
                        # print(f"cost: {cost}")
                        l_height_copy[i] = max_height + 1
                        max_height = l_height_copy[i]
                        print(f"updated max_height: {max_height}")
            costs.append(cost)

print(costs)
print(min(costs))

# ----- 方針 -----
# N > Kとする。
# i個目の建物高さを変更するとき1が立つN個のbitsを考える。
# bitが立っている建物の番号のリストを以下で求める。
# buildings = []
# for i in range(N):
#     if bits & (1 << i):
#         buildings.append(i)
# bitsのうち、K個bitが立っているものを考える。
# bitが立っている番号の建物が必ず見えるように高さを増やしたときのcostを求める。
