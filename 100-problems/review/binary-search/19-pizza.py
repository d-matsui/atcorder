#!/usr/bin/env python3

d = int(input())
n_shops = int(input())
m_orders = int(input())

shops = [0, d]
for _ in range(n_shops - 1):
    shop = int(input())
    shops.append(shop)
shops = sorted(shops)

orders = []
for _ in range(m_orders):
    order = int(input())
    orders.append(order)

# print(d, n_shops, m_orders, orders)


def is_ok(array, index, value):
    if array[index] >= value:
        return True
    return False


def bs_general(array, value, is_ok):
    left = -1
    right = len(array)
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if is_ok(array, mid, value):
            right = mid
        else:
            left = mid
    return right


total = 0
# print(f"shops = {shops}")
for order in orders:
    cost = float("inf")
    index = bs_general(shops, order, is_ok)
    for i in [index - 1, index, index + 1]:
        if 0 <= i <= len(shops) - 1:
            cost = min(cost, abs(shops[i] - order))
    total += cost

print(total)
