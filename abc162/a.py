#!/usr/bin/env python3

n = list(input())

flag = False
for i in range(3):
    if n[i] == '7':
        flag = True

if flag:
    print("Yes")
else:
    print("No")
