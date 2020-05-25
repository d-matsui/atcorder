#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)

n_teams, m_players = map(int, input().split())
candidates = list(map(int, input().split()))

res_set = set()
res = []
for i in reversed(range(n_teams)):
    candidate = candidates[i]
    if candidate not in res_set:
        res_set.add(candidate)
        res.append(candidate)

print(*res)
