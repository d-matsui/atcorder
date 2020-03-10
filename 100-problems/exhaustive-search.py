#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
# print(n, A)
# print(q, m)

flags = [False] * q
for i in range(2 ** n):
    if all(flags):
        break
    s = []
    for j in range(n):
        if i & (1 << j):
            s.append(A[j])
    for j in range(q):
        if m[j] == sum(s):
            flags[j] = True

for i in range(q):
    if flags[i]:
        print("yes")
    else:
        print("no")
