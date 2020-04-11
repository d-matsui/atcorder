#!/usr/bin/env python3

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
# print(N, A, B)

A, B = sorted(A), sorted(B)
start, goal = A[len(A) // 2], B[len(B) // 2]
# print(start, goal)

total = 0
for i in range(N):
    a, b = A[i], B[i]
    total += abs(start - a) + abs(a - b) + abs(b - goal)

print(total)
