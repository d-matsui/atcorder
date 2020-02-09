#!/usr/bin/env python3

N = int(input())

def isHandStand(A, B):
    A_str = str(A)
    B_str = str(B)
    if A_str[-1] == B_str[0] and A_str[0] == B_str[-1]:
        return True
    return False

count = 0
for A in range(1, N+1):
    for B in range(1, N+1):
        # print(A, B)
        if isHandStand(A, B):
            count += 1

print(count)
