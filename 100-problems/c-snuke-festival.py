#!/usr/bin/env python3

import bisect

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
# print(f"N: {N}")
# print(f"A, B, C: {A}, {B}, {C}")

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

# count = 0
# for bot in B:
#     # print(f"bot: {bot}")
#     index_A = binary_search_left(A, bot)
#     index_C = binary_search_right(C, bot)
#     # print(f"index_A: {index_A}, index_C: {index_C}")
#     count += index_A * (N - index_C)

# print(count)

count = 0
for bot in B:
    # print(f"bot: {bot}")
    index_A = bisect.bisect_left(A, bot)
    index_C = bisect.bisect_right(C, bot)
    # print(f"index_A: {index_A}, index_C: {index_C}")
    count += index_A * (N - index_C)

print(count)
