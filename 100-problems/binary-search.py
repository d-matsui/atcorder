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
    return None

print(binary_search(l, 101))

# 大人しくbisectを使いましょう...

# def binary_search_left(arr, value):
#     left = 0
#     right = len(arr) - 1
#     if value < arr[left]:
#         return left
#     if value > arr[right]:
#         return right + 1
#     while left <= right:
#         mid = (left + right) // 2
#         if value > arr[mid]:
#             left = mid + 1
#         elif value < arr[mid]:
#             right = mid - 1
#         else:
#             # find the leftmost index
#             while arr[mid] == value:
#                 mid -= 1
#             return mid + 1
#     # left == right + 1, so arr[right] < value < arr[left]
#     return left

# def binary_search_right(arr, value):
#     left = 0
#     right = len(arr) - 1
#     if value < arr[left]:
#         return left
#     if value > arr[right]:
#         return right + 1
#     while left <= right:
#         mid = (left + right) // 2
#         if value > arr[mid]:
#             left = mid + 1
#         elif value < arr[mid]:
#             right = mid - 1
#         else:
#             # find the leftmost index
#             while arr[mid] == value:
#                 if mid == len(arr) - 1:
#                     return mid + 1
#                 mid += 1
#             return mid
#     # left == right + 1, so arr[right] < value < arr[left]
#     return left

# def binary_search_closest(arr, value):
#     left = 0
#     right = len(arr) - 1
#     if value < arr[left]:
#         return left
#     if value > arr[right]:
#         return right

#     while left <= right:
#         mid = int((left + right) / 2)
#         if value > arr[mid]:
#             left = mid + 1
#         elif value < arr[mid]:
#             right = mid - 1
#         else:
#             return mid

#     # left == right + 1, so arr[right] < value < arr[left]
#     diff_left = arr[left] - value
#     diff_right = value - arr[right]
#     # return indevalue closest to value
#     return left if diff_left < diff_right else right

# def binary_search_closest_recursive(arr, value, left, right):
#     if left > right:
#         # left == right + 1, so arr[right] < value < arr[left]
#         diff_left = arr[left] - value
#         diff_right = value - arr[right]
#         # return index closest to value
#         return left if diff_left < diff_right else right

#     mid = int((left + right) / 2)
#     if value > arr[mid]:
#         return binary_search_closest_recursive(arr, value, mid + 1, right)
#     elif value < arr[mid]:
#         return binary_search_closest_recursive(arr, value, left, mid - 1)
#     else:
#         return mid
