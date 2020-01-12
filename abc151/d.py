#!/usr/bin/env python3

H, W = map(int, input().split())
S = []
for i in range(H):
    l = str(input())
    S.append(list(l))
# print(H, W)
# print(S)

# 迷路 S における (x1, y1) から (x2, y2) へ移動するのに要する最小 step 数
def min_steps(S, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        steps = 0
    else:
        steps = abs(x1 - x2) + abs(y1 - y2)
    return steps

max_steps = 0
for x1 in range(H):
    for y1 in range(W):
        if (S[x1][y1] != '#'):
            for x2 in range(H):
                for y2 in range(W):
                    if (S[x2][y2] != '#'):
                        steps = min_steps(S, x1, y1, x2, y2)
                        # print(steps)
                        if (steps > max_steps):
                            max_steps = min_steps(S, x1, y1, x2, y2)

print(max_steps)
