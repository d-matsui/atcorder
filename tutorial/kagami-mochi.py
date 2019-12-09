#!/usr/bin/env python

n = int(input())
d = []
for i in range(n):
    # print(i)
    d.append(int(input()))

# print(d)
d_set = set(d)
# print(d_set)
print(len(d_set))
