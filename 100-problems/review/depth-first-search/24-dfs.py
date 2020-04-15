#!/usr/bin/env python3

n = int(input())

edges = []
for _ in range(n):
    line = list(map(int, input().split()))
    v_list = [v - 1 for v in line[2:]]
    edges.append(v_list)
# print(n, edges)


def dfs(v):
    global time
    d[v] = time
    time += 1
    for v_next in edges[v]:
        if d[v_next] == -1:
            d[v_next] = time
            dfs(v_next)
    f[v] = time
    time += 1


d, f = [-1 for _ in range(n)], [-1 for _ in range(n)]
v_start = 0
time = 1
dfs(v_start)

for v in range(n):
    if d[v] == -1:
        dfs(v)

for v in range(n):
    print(v + 1, d[v], f[v])
