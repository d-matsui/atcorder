#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float("inf")

W, H = map(int, input().split())

# 上に H - 1 回、右に W - 1 回移動するときの組み合わせの数を求めればよい
# これは (H + W - 2) 回移動する中から、H - 1 (or W - 1) 回移動する方法の組み合わせの数になる
# {H+W-2}_C_{H-1} = (H + W - 2)! / (H - 1)! * (W - 1)!
# しかし、(H + W - 2)! や (H - 1)! * (W - 1)! は大きな数なので計算しきれない
# (H + W - 2)! を mod で割って余りを計算してしまうと、普通に割り算はできない

# M = 1,000,000,007 は素数なので、mod M での割り算は書け算に変換できる
# a^(p-1) \equiv 1 (mod p) より、a^(p-2) \equiv a^(-1) (mod p) が成り立つ

def modinv(a, mod):
    return pow(a, mod - 2, mod)


def enumfact(n, mod):
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= mod
    return res


def denomfact(n, mod):
    res = 1
    for i in range(1, n + 1):
        res *= modinv(i, mod)
        res %= mod
    return res


mod = 10 ** 9 + 7
ans = enumfact(H + W - 2, mod) * denomfact(H - 1, mod) * denomfact(W - 1, mod) % mod
print(ans)
