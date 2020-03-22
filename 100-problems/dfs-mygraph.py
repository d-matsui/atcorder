#!/usr/bin/env python3
from collections import defaultdict


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

    def remove(self, v):
        """ Remove all references to node v """

        for _, cxns in self._graph.items():
            try:
                cxns.remove(v)
            except KeyError:
                pass
        try:
            del self._graph[v]
        except KeyError:
            pass

    def get_adj(self, v):
        """ Get adjacency list of node v """
        return self._graph[v]

    def is_connected(self, u, v):
        """ Is node u directly connected to node v """

        return u in self._graph and v in self._graph[u]

    def find_path(self, src, dst, path=[]):
        """ Find any path from src node to dst node (may not be shortest) """

        path = path + [src]
        if src == dst:
            return path
        if src not in self._graph:
            return None
        for src_next in self._graph[src]:
            if src_next not in path:
                new_path = self.find_path(src_next, dst, path)
                if new_path:
                    return new_path
        return None

    def find_all_paths(self, src, dst, path=[]):
        """ Find all paths from src node to dst node """
        path = path + [src]
        if src == dst:
            return path
        if src not in self._graph:
            return None
        paths = []
        for src_next in self._graph[src]:
            if src_next not in path:
                new_path = self.find_all_paths(src_next, dst, path)
                if new_path:
                    paths.append(new_path)
        if len(paths) > 0:
            return paths
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


# -----
n = int(input())
adj_list = []
for _ in range(n):
    line = list(map(int, input().split()))
    v = line[0]
    adj_v = line[2:] if line[1] != 0 else []
    adj_list.append(adj_v)
# print(adj_list)

connections = []
for u in range(n):
    for v in adj_list[u]:
        connections.append((u + 1, v))
# print(connections)

g = Graph(connections, directed=True)
# print(g)

d = {}
f = {}
keys = [v for v in range(1, n + 1)]
values = [False for _ in range(n)]
seen = dict(zip(keys, values))
time = 0


def dfs(g, v):
    global time
    # print(f"discover {v}")
    time += 1
    d[v] = time
    # print(f"d[{v}] = {time}")
    seen[v] = True
    for v_next in g.get_adj(v):
        if not seen.get(v_next):
            dfs(g, v_next)
    # print(f"finish {v}")
    time += 1
    f[v] = time
    # print(f"f[{v}] = {time}")


for v in range(1, n + 1):
    if not seen[v]:
        dfs(g, v)

# print(f"seen: {seen}")
# print(f"d: {d}")
# print(f"f: {f}")
for v in range(1, n + 1):
    print(f"{v} {d[v]} {f[v]}")
