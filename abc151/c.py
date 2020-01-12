#!/usr/bin/env python3

N, M = map(int, input().split())
plist = [[] for i in range(N)]
for i in range(M):
    p, S = input().split()
    # plist の i 番目の要素: 問題 i-1 に対する提出結果のリスト
    plist[int(p) - 1].append(str(S))
# print(N, M)
# print(plist)

count_AC = 0
sum_penalty = 0
for l in plist:
    penalty = 0
    if 'AC' in l:
        count_AC += 1
        penalty = l.index('AC')
    sum_penalty += penalty

print(count_AC, sum_penalty)
