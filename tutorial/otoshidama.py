#!/usr/bin/env python

n, y = map(int, input().split())
# print(n, y)

found = False
for i in range(n+1):
    for j in range(n+1):
        if i + j > n:
            break
        k = n - (i + j)
        if 10000 * i + 5000 * j + 1000 * k == y and i + j + k == n:
            found = True
            print("{} {} {}".format(i, j, k))
            break
    if found:
        break

if not found:
    print("-1 -1 -1")
