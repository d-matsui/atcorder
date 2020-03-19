#!/usr/bin/env python3

N = int(input())
HS = []
for _ in range(N):
    l = list(map(int, input().split()))
    HS.append(l)

# 部分点がもらえる解法
# 高さの上限をhとしたとき、ある風船を何秒に以内に割らなければならないかが定まる。
# 風船iは、(h - H[i])/S[i] 秒以内に割らなければならない。
# 高さの上限hに達するまでに、全ての風船を割ることできるかを判定するには、
# 制限時間が短かいものから順に割っていくことができるかを調べればよい。
# hを徐々に大きくし、順に割ことのできるhの最小値を求めれば良い。
# 満点がもらえる解法
# 上記のようにしてhの最小値を求めるとき、二分探索を使って求める。

def can_finish(height, HS):
    limit = [(height - h) // s for h, s in HS]
    limit.sort()
    time = 0
    for l in limit:
        if l < time:
            return False
        time += 1
    return True

def binary_search(HS):
    left = 0
    right = 10 ** 14
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid, HS):
            right = mid
        else:
            left = mid + 1
    return right

score = binary_search(HS)
print(score)
