#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


N, M, Q = map(int, input().split())
trains = []
for _ in range(M):
    l, r = map(int, input().split())
    # 0-index
    trains.append([l-1, r-1])
# pprint(trains)
queries = []
for _ in range(Q):
    p, q = map(int, input().split())
    # 0-index
    queries.append([p-1, q-1])
# pprint(queries)

# s[l][r] := (0, 0) ~ (l-1, r-1) の領域に含まれる列車の数
# s[l+1][r+1] = s[l][r+1] + s[l+1][r] + A[l][r] - s[l][r]
s = [[0 for r in range(N+1)] for l in range(N+1)]

for l, r in trains:
    s[l+1][r+1] += 1

for l in range(N):
    for r in range(N):
        s[l+1][r+1] += s[l][r+1] + s[l+1][r] - s[l][r]

# s[q+1][q+1] - s[p][q+1] - s[q+1][p] + s[p][p]

for p, q in queries:
    ans = s[q+1][q+1] - s[p][q+1] - s[q+1][p] + s[p][p]
    print(ans)
