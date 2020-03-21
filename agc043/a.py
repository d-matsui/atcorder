#!/usr/bin/env python3

H, W = map(int, input().split())
square = []
for _ in range(H):
    line = list(input())
    square.append(line)

for h in range(H):
    for w in range(W):
        print(square[h][w], end='')
