#!/usr/bin/env python3

n = int(input())
adj = {}
for _ in range(n):
    line = list(map(int, input().split()))
    v = line[0]
    adj_v = line[2:] if line[1] != 0 else []
    adj.setdefault(v, adj_v)
# print(f"adj: {adj}")

m = sum([len(adj.get(v)) for v in range(1, n + 1)])
d = {}
f = {}
v_list = [v for v in range(1, n + 1)]
hasSeen_list = [False for _ in range(n)]
seen = dict(zip(v_list, hasSeen_list))

time = 0


def dfs(adj, v):
    global time
    # print(f"discover {v}")
    time += 1
    d[v] = time
    # print(f"d[{v}] = {time}")
    seen[v] = True
    for v_next in adj.get(v):
        if not seen.get(v_next):
            dfs(adj, v_next)
    # print(f"finish {v}")
    time += 1
    f[v] = time
    # print(f"f[{v}] = {time}")


v = 1
time = 0

for v in range(1, n + 1):
    if not seen[v]:
        dfs(adj, v)

# print(f"seen: {seen}")
# print(f"d: {d}")
# print(f"f: {f}")
for v in range(1, n + 1):
    print(f"{v} {d[v]} {f[v]}")
