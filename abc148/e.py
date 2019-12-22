#!/usr/bin/env python

n_int = int(input())
n_str = str(n_int)
# print(n_int)
# print(len(n_str))

def num_to_keta(num):
    return(len(str(num)) - 1)

def g(n):
    print(n)
    if n == 10:
        return 1
    else:
        return num_to_keta(n) + g(int(n/10))

flag = False
if n_int < 10 or n_int % 2 != 0:
    flag = True

if flag:
    print(0)
else:
    n = num_to_keta(n_int) * 10
    print(g(n))
