#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

a_copy = a
is_possible = 1 in a_copy
num = 0
i = 0
if is_possible:
    while True:
        num += 1
        if num in a_copy:
            # print(num, 'is in a_copy', a_copy.index(num))
            a_copy = a_copy[a_copy.index(num):]
            # print('a_copy', a_copy)
        else:
            print('break')
            # print('num = ', num)
            break

if is_possible:
    print(len(a) - (num - 1))
else:
    print(-1)
