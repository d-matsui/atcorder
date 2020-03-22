#!/usr/bin/env python3
from graph_tools import Graph

connections = [(1, 2), (2, 3), (3, 1), (3, 4)]

g = Graph(connections)
print(g._graph)

print("add (1, 5)")
g.add(1, 5)
print(g._graph)

print("remove 5")
g.remove(5)
print(g._graph)

print(g.get_adj(1))

print(f"(1, 2) is connected:", g.is_connected(1, 2))
print(f"(2, 3) is connected:", g.is_connected(2, 3))
print(f"find_path from 1 to 4:", g.find_path(1, 4))

