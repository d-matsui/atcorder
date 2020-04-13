#!/usr/bin/env python3

N = int(input())
S = list(input())

n_r, n_g, n_b = 0, 0, 0
for i in range(N):
    if S[i] == 'R':
        n_r += 1
    elif S[i] == 'G':
        n_g += 1
    else:
        n_b += 1
# print(n_r, n_g, n_b)

n_ignore = 0
for i in range(N):
    for j in range(N):
        k = 2 * j - i
        if k >= N:
            continue
        cond_first = i < j < k
        cond_second = S[i] != S[j] and S[i] != S[k] and S[j] != S[k]
        if cond_first and cond_second:
            n_ignore += 1

res = n_r * n_g * n_b - n_ignore
print(res)
