#!/usr/bin/env python3
import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
# print(N, K)
# print(A)

# X is a list of integer
def f(X):
    return max(X) - min(X)

combs = list(itertools.combinations(A, K))
# print(combs)
total = 0
for comb in combs:
    total += f(comb)

mod = 10^9 + 7
print(total % mod)
