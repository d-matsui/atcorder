#!/usr/bin/env python3

a, b = map(int, input().split())

a_str = ''
for i in range(b):
    a_str += str(a)

b_str = ''
for i in range(a):
    b_str += str(b)

# print(a_str, b_str)

if a_str == b_str:
    print(a_str)
elif a_str > b_str:
    print(b_str)
else:
    print(a_str)
