#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


# 入力をグラフで表現し、K ホップ以下の経路のうち重みの和が最大の経路を求めたい
# あるサイクルの重みの和が正なら、そのサイクルを周れるだけ周った方が重みの和は大きくなる
# ここで、あるサイクルに含まれる経路を考える (ただし、その経路は当該サイクルを巡回しない)
# そのような経路のうち、重みが最大の経路を見つけ、(周った方が特なら) サイクルを周れるだけ周った際 の重み和と、その経路の重み和の合計を計算すれば、それがそのサイクルにおける重み和最大の経路である
# 複数サイクル存在する場合は、各サイクルについて上記の和を求め、その最大値を出力すれば良い

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

adj_list = [[] for _ in range(len(P))]
for u, v in enumerate(P):
    # 0-index
    v -= 1
    adj_list[u].append([v, C[v]])
# pprint(adj_list)

