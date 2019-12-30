#!/usr/bin/env python

n, m = map(int, input().split())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

cmd_list = list(input())

def rotate_90(arr):
    return [list(reversed(l)) for l in zip(*arr)]

def rotate(arr, degrees):
    if degrees == 90:
        arr = rotate_90(arr)
    if degrees == 180:
        arr = rotate_90(arr)
        arr = rotate_90(arr)
    if degrees == -90:
        arr = rotate_90(arr)
        arr = rotate_90(arr)
        arr = rotate_90(arr)
    return arr

def left(arr):
    len_row = len(arr)
    len_column = len(arr[0])
    for i in range(len_row):
        for j in range(len_column - 1):
            # composition
            if arr[i][j] == arr[i][j+1]:
                arr[i][j] = 2 * arr[i][j]
                arr[i][j+1] = 0
        # move zero to right
        arr[i] = [num for num in arr[i] if num != 0]
        for k in range(len_column - len(arr[i])):
            arr[i].append(0)
    return arr

for cmd in cmd_list:
    if(cmd == 'L'):
        left(arr)
    if(cmd == 'R'):
        arr = rotate(arr, 180)
        left(arr)
        arr = rotate(arr, 180)
    if(cmd == 'U'):
        arr = rotate(arr, -90)
        left(arr)
        arr = rotate(arr, 90)
    if(cmd == 'D'):
        arr = rotate(arr, 90)
        left(arr)
        arr = rotate(arr, -90)

for num in arr:
    print(*num)
