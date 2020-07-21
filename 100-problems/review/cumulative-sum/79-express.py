#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M, Q = map(int, input().split())
L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

queries = []
for _ in range(Q):
    p, q = map(int, input().split())
    # 0-index
    queries.append([p, q])


# s[l][r] := (0, 0), (l, r) の領域に含まれる列車の数
# s[l][r] = s[l-1][r] + s[l][r-1] - s[l-1][r-1] + a[l][r]

s = [[0 for r in range(N+1)] for l in range(N+1)]
for i in range(M):
    s[L[i]][R[i]] += 1

for l in range(1, N+1):
    for r in range(1, N+1):
        s[l][r] += s[l-1][r] + s[l][r-1] - s[l-1][r-1]

for l, r in queries:
    ans = s[r][r] - s[l-1][r] - s[r][l-1] + s[l-1][l-1]
    print(ans)
