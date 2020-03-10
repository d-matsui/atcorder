#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
# print(n, A)
# print(q, m)

S = []
for i in range(2 ** n):
    s = []
    for j in range(n):
        if i & (1 << j):
            s.append(A[j])
    S.append(s)
# print(S)

for i in range(q):
    flag = False
    for j in range(len(S)):
        if m[i] == sum(S[j]):
            flag = True
            break
    if flag:
        print("yes")
    else:
        print("no")
