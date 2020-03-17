#!/usr/bin/env python3

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
# print(n, S, q, T)

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1

S.sort()
count = 0
for i in range(q):
    if binary_search(S, T[i]) != -1:
        count += 1

print(count)
