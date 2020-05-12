#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


n_queries = int(input())
queries = []
for _ in range(n_queries):
    l, r = map(int, input().split())
    queries.append([l, r])

MAX_INT = 10 ** 5


def eratos(number):
    is_prime = [1] * (number + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, number + 1):
        if not is_prime[i]:
            continue
        j = i + i
        while j < number + 1:
            is_prime[j] = 0
            j += i
    return is_prime


def like(number):
    is_like = [0] * (number + 1)
    for i in range(number + 1):
        if i % 2 == 0:
            continue
        if is_prime[i] and is_prime[(i + 1) // 2]:
            is_like[i] = 1
    return is_like


is_prime = eratos(MAX_INT)
is_like = like(MAX_INT)

cum_sum = [0] * (MAX_INT + 2)
for i in range(MAX_INT + 1):
    cum_sum[i+1] = cum_sum[i] + is_like[i]

for l, r in queries:
    res = cum_sum[r+1] - cum_sum[l]
    print(res)
