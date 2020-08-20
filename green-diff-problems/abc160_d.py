#!/usr/bin/env python3

from pprint import pprint
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


# s, t \in V (s < t) に対して、s から t への最短経路を d_min(s, t) とすると、
# d_min(s, t) は、
# d_min(s, t) = min(t - s, abs(x - s) + 1 + abs(t - y))
# で与えられる。
# なので、s, t の全ての組み合わせに対して d_min(s, t) を計算し、条件を満たすような s, t の組を数え上げればよい。


N, X, Y = map(int, input().split())
# 0-index
X -= 1
Y -= 1

count_dict = defaultdict(int)

# O(N^2)
for s in range(N - 1):
    for t in range(s + 1, N):
        dist = min(t - s, abs(X - s) + 1 + abs(t - Y))
        count_dict[dist] += 1

for k in range(1, N):
    ans = 0
    if k in count_dict:
        ans = count_dict[k]
    print(ans)
