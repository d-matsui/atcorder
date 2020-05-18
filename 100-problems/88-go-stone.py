#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n = int(input())
stones = []
for _ in range(n):
    stones.append(int(input()))
# pprint(stones)

seq_white = [0] * n
seq_black = [0] * n

res = 0
if stones[0] == 0:
    res += 1
    seq_white[0] += 1
else:
    seq_black[0] += 1


def is_white(stone):
    return stone == 0


for i in range(1, n):
    stone = stones[i]
    if i % 2 == 1:
        prev_stone = stones[i - 1]
        if stone == prev_stone:
            # 偶数回目のとき、直前に置いた碁石と同色なら、単に碁石を右端に置く
            if is_white(stone):
                res += 1
                # print(f'i = {i}, res = {res}')
                seq_white[i] = seq_white[i - 1] + 1
                seq_black[i] = 0
            else:
                seq_white[i] = 0
                seq_black[i] = seq_black[i - 1] + 1
        else:
            # 偶数回目のとき、直前に置いた碁石と異なる色なら、
            # 右端の連続した同色の碁石全てを置く碁石に替え、右端に碁石を置く
            if is_white(stone):
                res += seq_black[i - 1] + 1
                seq_white[i] = seq_black[i - 1] + 1 + seq_white[i - 1 - seq_black[i - 1]]
                seq_black[i] = 0
            else:
                res = min(0, res - seq_white[i - 1])
                # print(f'i = {i}, res = {res}')
                seq_white[i] = 0
                seq_black[i] = seq_white[i - 1] + 1 + seq_black[i - 1 - seq_black[i - 1]]
    else:
        # 奇数回目のとき、単に碁石を右端に置く
        if is_white(stone):
            res += 1
            # print(f'i = {i}, res = {res}')
            seq_white[i] = seq_white[i - 1] + 1
            seq_black[i] = 0
        else:
            seq_white[i] = 0
            seq_black[i] = seq_black[i - 1] + 1

# print(seq_white)
# print(seq_black)
print(res)

