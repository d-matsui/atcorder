#!/usr/bin/env python3

N = int(input())
A = [[] for i in range(N)]

for i in range(0, N):
    Ai = int(input())
    for j in range(0, Ai):
        l = list(map(int, input().split()))
        A[i].append(l)
# print(A)

l = [[] for i in range(N)]
for num in range(2 ** N):
    bits = bin(num)
    # print(bits)
