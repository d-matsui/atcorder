#!/usr/bin/env python3

from pprint import pprint
from bisect import bisect_left
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
# print(N, A)

# 到着する順番は降順が最適
# 足せる回数は合計 N-1 回
# 最初の数字は 1 回、他は高々 2 回足される

ans = 0
times = N - 1

for i in range(N):
    limit = 2
    if i == 0:
        limit = 1
    for _ in range(limit):
        if times > 0:
            ans += A[i]
            times -= 1

print(ans)
