#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
inf = float("inf")

Q = int(input())
queries = []

for _ in range(Q):
    l, r = map(int, input().split())
    queries.append([l, r])
# print(queries)

MAX = 10 ** 5 + 1

# Sieve of Eratosthenes
is_prime = [1 for _ in range(MAX)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, MAX):
    if not is_prime[i]:
        continue
    j = i + i
    while j < MAX:
        is_prime[j] = 0
        j += i

a = [0 for _ in range(MAX)]
for i in range(MAX):
    if i % 2 == 0:
        continue
    if is_prime[i] and is_prime[(i + 1) // 2]:
        a[i] = 1

cum_sum = [0 for _ in range(MAX + 1)]
for i in range(MAX):
    cum_sum[i + 1] = cum_sum[i] + a[i]

for left, right in queries:
    # print(f"s[left] = {cum_sum[left]}")
    # print(f"s[right] = {cum_sum[right]}")
    x = cum_sum[right + 1] - cum_sum[left]
    print(x)
