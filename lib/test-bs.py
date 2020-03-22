#!/usr/bin/env python3

def bs(array, key, is_ok):
    left = -1
    right = len(array)

    while abs(right - left) > 1:
        mid = (left + right) // 2
        if is_ok(array, mid, key):
            right = mid
        else:
            left = mid
    return right

def is_eq_or_more(array, index, key):
    if array[index] >= key:
        return True
    return False

def is_more(array, index, key):
    if array[index] > key:
        return True
    return False

arr = [1, 3, 4, 4, 4, 5, 7]
print(f"arr: {arr}")

keys = [1, 2, 3, 4, 5, 6, 7, 8]
print("equal or more than")
for key in keys:
    print(f"bs {key}: {bs(arr, key, is_eq_or_more)}")

print("more than")
for key in keys:
    print(f"bs {key}: {bs(arr, key, is_more)}")
