#!/usr/bin/env python3

N, K = map(int, input().split())
l_height = list(map(int, input().split()))
# print(N, K)
# print(l_height)

costs = []
if N == K:
    cost = 0
    prev_height = l_height[0]
    for i in range(1, N):
        if prev_height >= l_height[i]:
            cost += prev_height - l_height[i] + 1
            l_height[i] = prev_height + 1
        prev_height = l_height[i]
    costs.append(cost)
else:
    for bits in range(2 ** N):
        l_height_copy = l_height[:]
        buildings = []
        for i in range(N):
            if bits & (1 << i):
                buildings.append(i)
        cost = 0
        if len(buildings) == K:
            # print(f"bits: {bin(bits)}")
            # print(f"buildings: {buildings}")
            prev_height = l_height_copy[0]
            for i in range(1, N):
                if i in buildings:
                    # print(f"i: {i} is in buildings")
                    # print(f"buildings: {buildings}")
                    # print(f"l_height_copy: {l_height_copy}")
                    # print(f"prev_height: {prev_height}")
                    # print(f"l_height_copy[i]: {l_height_copy[i]}")
                    if prev_height >= l_height_copy[i]:
                        # print("prev_height >= l_height[i]")
                        cost += prev_height - l_height_copy[i] + 1
                        # print(f"cost: {cost}")
                        l_height_copy[i] = prev_height + 1
                        prev_height = l_height_copy[i]
                        # print(f"updated prev_height: {prev_height}")
                else:
                    if l_height_copy[i] > prev_height:
                        # print(f"updated prev_height: {prev_height}")
                        prev_height = l_height_copy[i]
            costs.append(cost)

# print(costs)
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
