#!/usr/bin/env python3
from graph_tools import Graph
import pprint

connections = [(1, 2), (1, 3), (2, 3), (1, 4)]

g = Graph(connections)
pprint.pprint(g._graph)

g.add(1, 5)
pprint.pprint(g._graph)

g.remove(5)
pprint.pprint(g._graph)

print('1, 2 is connected:', g.is_connected(1, 2))
print('2, 4 is connected:', g.is_connected(2, 4))

print('find_path from 1 to 4:', g.find_path(1, 4))
