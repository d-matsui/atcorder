#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


X, Y, A, B, C = map(int, input().split())
apples_A = sorted(list(map(int, input().split())))
apples_B = sorted(list(map(int, input().split())))
apples_C = sorted(list(map(int, input().split())))

# 赤のリンゴからおいしさが大きい順に X 個選ぶ (1)
# 緑のリンゴからおいしさが大きい順に Y 個選ぶ (2)
# (1), (2) そして 無色のリンゴのから、おいしさが大きいものから順に X + Y 個選べば良い

apples_rest = sorted(apples_A[-X:] + apples_B[-Y:] + apples_C)
ans = sum(apples_rest[ -(X + Y):])

print(ans)
