#!/usr/bin/env python3

import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
# print(N, M)
# print(A)

perms = list(itertools.permutations(A, 2))
for i in A:
    perms.append((i, i))

def sum(a, b):
    return a + b

sum_list = []
for perm in perms:
    a = perm[0]
    b = perm[1]
    sum_list.append(sum(a, b))

# for l in sum_list:
#     print(l)

result = 0
for i in range(M):
    index_max = sum_list.index(max(sum_list))
    result += sum_list.pop(index_max)

print(result)
