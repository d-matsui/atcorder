#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

N, K = map(int, input().split())

# x (= 10 ** 100) の係数がaのとき、和としてあり得るものの個数は何個あるかを考える
# K <= a <= N + 1

b_list = range(N + 1)

ans = 0
for a in range(K, N + 2):
    # print(f"a = {a}")
    b_min = a * (a - 1) / 2
    b_max = a / 2 * (2 * (N - (a - 1)) + a - 1)
    # print(f"b_min = {b_min}, b_max = {b_max}")
    ans += b_max - b_min + 1

print(int(ans) % (10 ** 9 + 7))
