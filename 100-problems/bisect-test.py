#!/usr/bin/env python3

import bisect

l = [1, 3, 3, 5]

print("bisect")

# print(bisect.bisect_left(l, 0))
# print(bisect.bisect_right(l, 0))
# print(bisect.bisect_left(l, 1))
# print(bisect.bisect_right(l, 1))
# print(bisect.bisect_left(l, 2))
# print(bisect.bisect_right(l, 2))
# print(bisect.bisect_left(l, 3))
# print(bisect.bisect_right(l, 3))
# print(bisect.bisect_left(l, 5))
# print(bisect.bisect_right(l, 5))
# print(bisect.bisect_left(l, 6))
# print(bisect.bisect_right(l, 6))

def binary_search_left(arr, value):
    left = 0
    right = len(arr) - 1
    if value < arr[left]:
        return left
    if value > arr[right]:
        return right + 1
    while left <= right:
        mid = (left + right) // 2
        if value > arr[mid]:
            left = mid + 1
        elif value < arr[mid]:
            right = mid - 1
        else:
            # find the leftmost index
            while arr[mid] == value:
                mid -= 1
            return mid + 1
    # left == right + 1, so arr[right] < value < arr[left]
    return left

def binary_search_right(arr, value):
    left = 0
    right = len(arr) - 1
    if value < arr[left]:
        return left
    if value > arr[right]:
        return right + 1
    while left <= right:
        mid = (left + right) // 2
        if value > arr[mid]:
            left = mid + 1
        elif value < arr[mid]:
            right = mid - 1
        else:
            # find the leftmost index
            while arr[mid] == value:
                if mid == len(arr) - 1:
                    return mid + 1
                mid += 1
            return mid
    # left == right + 1, so arr[right] < value < arr[left]
    return left

print("my binary_search")
print(binary_search_left(l, 0))
print(binary_search_right(l, 0))
print(binary_search_left(l, 1))
print(binary_search_right(l, 1))
print(binary_search_left(l, 2))
print(binary_search_right(l, 2))
print(binary_search_left(l, 3))
print(binary_search_right(l, 3))
print(binary_search_left(l, 5))
print(binary_search_right(l, 5))
print(binary_search_left(l, 6))
print(binary_search_right(l, 6))

