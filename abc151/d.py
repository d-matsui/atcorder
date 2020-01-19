#!/usr/bin/env python3
from graph_tools import Graph
from collections import deque
import pprint

H, W = map(int, input().split())
S = []
for i in range(H):
    l = str(input())
    S.append(list(l))
# print(H, W)
# print(S)

connections = []

g = Graph(connections)
dist = [-1 for i in range(H * W)]
dq = deque()

# init
dq.append(0)
dist[0] = 0

while dq != []:
    v = dq.pop()
    for v_adj in g.adjacency_list():
        # undiscovered vertex
        if (dist[v_adj] == -1):
            dist[v_adj] = dist[v] + 1
            dq.append(v_adj)

pprint(dq)
pprint(dist)
