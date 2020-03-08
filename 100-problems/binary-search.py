#!/usr/bin/env python3

N = 100
l = list(range(N))

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

print(binary_search(l, 101))
