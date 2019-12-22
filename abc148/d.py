#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

flag = False
a_copy = a
num = 0
i = 0
while True:
    num += 1
    if num in a_copy:
        if num == 1:
            flag = True
        # print(num, 'is in a_copy', a_copy.index(num))
        a_copy = a_copy[a_copy.index(num):]
        # print('a_copy', a_copy)
    else:
        # print('break')
        # print('num = ', num)
        break

if flag:
    print(len(a) - (num - 1))
else:
    print(-1)
