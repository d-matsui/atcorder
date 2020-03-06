#!/usr/bin/env python3

A, B, C, X, Y = map(int, input().split())

# ABセット(ABピザ2枚)をi個購入したとき、
# Aをmax(0, X-i)個買い増す必要があり、Bをmax(0, Y-i)個買い増す必要がある。
# 0 <= i <= 10^5 について、全探索し、最小値を求めればよい

price_min = 5000 * 2 * 100000
for i in range(0, 100000+1):
    price = 2*C*i + A * max(0, X-i) + B * max(0, Y-i)
    if price < price_min:
        price_min = price

print(price_min)

# 定数時間でも解けるが、以下では不十分
# if (A+B) / 2 < C:
#     print("(A+B) / 2 < C")
#     # A, B それぞれ単品で買う方が得
#     total = A*X + B*Y
# else:
#     # A, B どちらかが十分な枚数になるまでABを買い残ったものを単品で買う or ABでどちらも十分な枚数で買う方が特
#     print("(A+B) / 2 >= C")
#     if A >= B:
#         print("A >= B")
#         total = C*X*2 + A * (Y-X)
#     else:
#         print("A < B")
#         total = C*Y*2 + A * (X-Y)
#         if C * X > total:
#             total = C * Y
#     num = X * 2 if X >= Y else Y * 2
#     print("num:", num)
#     print("total:", total)
#     print("C * num:", C * num)
#     if C * num < total:
#         total = C * num

# print(total)
