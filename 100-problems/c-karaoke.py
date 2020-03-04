#!/usr/bin/env python3

import itertools

N, M = map(int, input().split())

A = []
for i in range(N):
    l = list(map(int, input().split()))
    A.append(l)

# print(A)
# print(A[0][1])

l_T = itertools.combinations(range(M), 2)
# for T in l_T:
#     print(T[0], T[1])

score_max = 0
for T in l_T:
    score = 0
    for student in range(N):
        # print(A[student][T[0]], A[student][T[1]])
        score_student = A[student][T[0]] if A[student][T[0]] > A[student][T[1]] else A[student][T[1]]
        # print(score_student)
        score += score_student
    if score > score_max:
        score_max = score

print(score_max)
