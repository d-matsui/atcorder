#!/usr/bin/env python

n = int(input())
s, t = input().split()
# print(n, s, t)

str = []
for i in range(n):
    # print(i)
    str.append(s[i])
    str.append(t[i])

print(''.join(str))
