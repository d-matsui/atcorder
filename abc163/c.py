#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline

n = int(input())
a = list(map(int, input().split()))

ans = [0 for _ in range(n)]
for a_i in a:
    ans[a_i - 1] += 1

for i in range(n):
    print(ans[i])
