#!/usr/bin/env python3

import sys
from collections import defaultdict

input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 6)


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for u, v in connections:
            self.add(u, v)

    def add(self, u, v):
        """ Add connection between node u and node v """

        self._graph[u].add(v)
        if not self._directed:
            self._graph[v].add(u)

    def get_adj(self, v):
        """ Get adjacency list of node v """
        return self._graph[v]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


# -----
N, Q = map(int, input().split())
connections = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    connections.append((a, b))
query = []
for _ in range(Q):
    p, x = map(int, input().split())
    query.append([p, x])
# print(N, Q)
# print(connections, query)

keys = [v for v in range(1, N + 1)]
values = [0 for _ in range(N)]
counter = dict(zip(keys, values))
# print(counter)
for p, x in query:
    counter[p] += x


def dfs(v, parent):
    for v_next in g.get_adj(v):
        if v_next != parent:
            counter[v_next] += counter.get(v)
            dfs(v_next, v)


g = Graph(connections)
# print(g)

root = 1
dfs(root, None)

for c in counter.values():
    print(c, end=" ")
