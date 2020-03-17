#!/usr/bin/env python3

len_ring = int(input())
n_shops = int(input())
m_order = int(input())

shops = [0, len_ring]
for i in range(n_shops-1):
    shops.append(int(input()))
# shops = sorted(shops)
shops.sort()

orders = []
for i in range(m_order):
    orders.append(int(input()))

def binary_search_closest(arr, value):
    left = 0
    right = len(arr) - 1
    if value < arr[left]:
        return arr[left]
    if value > arr[right]:
        return arr[right]

    while left <= right:
        mid = int((left + right) / 2)
        if value > arr[mid]:
            left = mid + 1
        elif value < arr[mid]:
            right = mid - 1
        else:
            return mid

    # left == right + 1, so arr[right] < value < arr[left]
    diff_left = arr[left] - value
    diff_right = value - arr[right]
    # return index closest to value
    return left if diff_left < diff_right else right

def binary_search_closest_recursive(arr, value, left, right):
    if left > right:
        # left == right + 1, so arr[right] < value < arr[left]
        diff_left = arr[left] - value
        diff_right = value - arr[right]
        # return index closest to value
        return left if diff_left < diff_right else right

    mid = int((left + right) / 2)
    if value > arr[mid]:
        return binary_search_closest_recursive(arr, value, mid + 1, right)
    elif value < arr[mid]:
        return binary_search_closest_recursive(arr, value, left, mid - 1)
    else:
        return mid

sum = 0
for order in orders:
    # 配達先に最も近い店舗
    index = binary_search_closest(shops, order)
    # left = 0
    # right = n_shops - 1
    # index = binary_search_closest_recursive(shops, order, left, right)
    start = shops[index]
    end = order
    if start <= end:
        dist_clockwise = end - start
        dist_counter_clockwise = len_ring - (end - start)
    else:
        dist_clockwise = len_ring - (start - end)
        dist_counter_clockwise = start - end
    sum += min(dist_clockwise, dist_counter_clockwise)

print(sum)
