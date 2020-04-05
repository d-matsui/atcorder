#!/usr/bin/env python3

a, b, c, x, y = map(int, input().split())

# ABセットをi個購入したとき、Aをmax(0, x - i)個、Bをmax(0, y - i)個購入する必要がある
# 1 <= x, y <= 10^5なので、全探索して最小金額を求めればよい

inf = float("inf")
min_price = inf
max_i = 10 ** 5

for i in range(max_i + 1):
    rest_x, rest_y = max(0, x - i), max(0, y - i)
    price = 2 * c * i + a * rest_x + b * rest_y
    if price < min_price:
        min_price = price

print(min_price)
