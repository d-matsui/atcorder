#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

l = []
isUnique = True
for i in range(len(A)):
    if A[i] in l:
        isUnique = False
        break
    l.append(A[i])

if isUnique:
    print("YES")
else:
    print("NO")
