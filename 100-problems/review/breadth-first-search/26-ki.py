#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


N, Q = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    # undirected, 0-indexed
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

query = []
for _ in range(Q):
    p, x = map(int, input().split())
    query.append([p - 1, x])

# 方針
# 1. 各クエリに対し、頂点p_jのカウンターにx_jを足す
# (この段階では部分木に含まれるノードには操作を行わない)
# 2. クエリを全て処理したあと、深さ優先順に各ノードvのカウンタを以下のように更新する
# count[v] = count[v] + 親ノードのカウンタ
# 毎回部分木に対して処理を行うのだとO(N^2)の計算量となり遅いので、上記のように工夫して更新する


def bfs(v, parent):
    for v_adj in graph[v]:
        if v_adj == parent:
            continue
        count[v_adj] += count[v]
        bfs(v_adj, v)


count = [0] * N
for p, x in query:
    count[p] += x
# pprint(count)

v = 0
bfs(0, -1)

print(*count)
