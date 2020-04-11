#!/usr/bin/env python3

# 1 <= K <= N <= 15
# 1 <= a_i <= 10 ** 9

N, K = map(int, input().split())
heights = list(map(int, input().split()))
# print(N, K, heights)


def calc(i, heights):
    cost = 0
    for shift in range(1, N):
        if i & (1 << shift):
            max_h = max(heights[:shift])
            if max_h >= heights[shift]:
                cost += (max_h + 1) - heights[shift]
                heights[shift] = max_h + 1
    return cost


str_bin = ""
for _ in range(K):
    str_bin += "1"
min_i = int(str_bin, 2)
min_cost = float("inf")


def is_valid(i, K):
    count = 0
    for bit in range(N):
        if i & (1 << bit):
            count += 1
    if count == K:
        return True
    return False


for i in range(min_i, 2 ** N):
    if is_valid(i, K):
        heights_copy = heights[:]
        # print(f"i = {i} ({bin(i)})")
        cost = calc(i, heights_copy)
        # print(f"cost = {cost}")
        min_cost = min(min_cost, cost)

print(min_cost)
