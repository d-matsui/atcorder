#!/usr/bin/env python3

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
# print(N, K, M)
# print(A)

# 平均点を M 点以上にできない場合
if (sum(A) + K) / N < M:
    score = -1
# 既に平均点が M 点以上の場合
elif sum(A) / N > M:
    score = 0
else:
    score = int(N * M - sum(A))

print(score)
