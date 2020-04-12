#!/usr/bin/env python3


def bs_normal(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] < value:
            left = mid + 1
        elif array[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1


def is_ok(array, index, value):
    if array[index] >= value:
        return True
    return False


def bs_general(array, value, is_ok):
    left = -1
    right = len(array)
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if is_ok(array, mid, value):
            right = mid
        else:
            left = mid
    return right


array = [1, 3, 4, 4, 4, 5, 7]
values = [1, 2, 3, 4, 5, 6, 7, 8]
print(array)
print("equal or more")
for value in values:
    print(f"(meguru) value = {value}, index = {bs(array, value, is_ok)}")
    print(f"(normal) value = {value}, index = {bs_normal(array, value)}")
