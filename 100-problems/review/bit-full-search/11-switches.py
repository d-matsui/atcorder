#!/usr/bin/env python3

N, M = map(int, input().split())

l_k = []
switches = []
for _ in range(M):
    line = list(map(int, input().split()))
    l_k.append(line[0])
    s = [i - 1 for i in line[1:]]
    switches.append(s)
l_p = list(map(int, input().split()))

# print(N, M)
# print(l_k, switches, l_p)

res = 0
for num in range(2 ** N):
    on_all = True
    for i in range(M):
        n_on = 0
        for s in switches[i]:
            if num & (1 << s):
                n_on += 1
        if n_on % 2 != l_p[i]:
            on_all = False
    if on_all:
        res += 1

print(res)
