#!/usr/bin/env python

import itertools

n, m = map(int, input().split())
l_list = list(map(int, input().split()))
# print(n, m)
# print(l_list)

perms = itertools.permutations(l_list, 3)
# for p in perms:
#     print(p)
def is_right_triangle(a, b, c):
    if (a*a + b*b == c*c):
        # print(a, b, c)
        return True
    return False

# print(is_right_triangle(3, 4, 5))

count = 0
for p in perms:
    a = p[0]
    b = p[1]
    c = p[2]
    if (is_right_triangle(a, b, c)):
        count += 1

print(count)
