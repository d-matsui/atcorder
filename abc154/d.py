#!/usr/bin/env python3

N, K = map(int, input().split())
p = list(map(int, input().split()))

def max_sum_section(arr, k):
    res = 0
    # TODO: i から i+k までの区間和が最大である区間を求めよ
    return res

def e_dice(n):
    res = 0
    for i in range(1, n+1):
        res += i * (1 / n)
    return res

res = 0
sec = max_sum_section(p, K)
for i in range(K):
    res += e_dice(sec[i])

print(res)
