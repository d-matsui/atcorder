#!/usr/bin/env python3

S = list(input())
T = list(input())

if len(T) == len(S) + 1:
    flag = True
    for i in range(len(S)):
        if S[i] != T[i]:
            flag = False
    if flag:
        print('Yes')
    else:
        print('No')
else:
    print('No')
