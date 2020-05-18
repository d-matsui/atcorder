#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n = int(input())
stones = [-1]
for _ in range(n):
    stones.append(int(input()))


def is_white(stone):
    return stone == 0


seq_white = [0] * (n + 1)
seq_black = [0] * (n + 1)

if is_white(stones[1]):
    seq_white[1] = 1
else:
    seq_black[1] = 1

res = 0
for i in range(1, n + 1):
    stone = stones[i]
    prev_stone = stones[i - 1]
    # 奇数回目 or 同色の碁石
    if i % 2 == 0 or stone == prev_stone:
        if is_white(stone):
            res += 1
            seq_white[i] = seq_white[i - 1] + 1
            seq_black[i] = 0
        else:
            seq_black[i] = seq_black[i - 1] + 1
            seq_white[i] = 0
    else:
        if is_white(stone):
            res += seq_black[i - 1] + 1
            seq_white[i] = seq_black[i - 1] + 1 + seq_white[i - 1 - seq_black[i - 1]]
            seq_black[i - 1] = 0
        else:
            res -= seq_white[i - 1]
            seq_black[i] = seq_white[i - 1] + 1 + seq_black[i - 1 - seq_white[i - 1]]
            seq_white[i - 1] = 0

print(res)
