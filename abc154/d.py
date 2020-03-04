#!/usr/bin/env python3
import copy

N, K = map(int, input().split())
p = list(map(int, input().split()))

def max_sum_section(arr, k):
    sec = []
    for i in range(k):
        sec.append(arr[i])
    max_sec = copy.deepcopy(sec)
    # TODO: i から i+k-1 までの区間和が最大である区間を求めよ
    for i in range(k, len(arr)):
        sec.pop(0)
        sec.append(arr[i])
        if sum(sec) > sum(max_sec):
            max_sec = copy.deepcopy(sec)
    return max_sec

# def e_dice(n):
#     res = 0
#     for i in range(1, n+1):
#         res += i * (1 / n)
#     return res

res = 0
sec = max_sum_section(p, K)
# for i in range(K):
#     res += e_dice(sec[i])



print(res)
