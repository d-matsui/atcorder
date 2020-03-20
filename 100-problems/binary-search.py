#!/usr/bin/env python3

def is_ok(array, index, value):
    if array[index] >= value:
        return True
    return False

def bs(array, value, is_ok):
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
    print(f"value = {value}, index = {bs(array, value, is_ok)}")
