#!/usr/bin/env python3

N = int(input())
H, S = [], []
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)
# print(N, H, S)

penalties = [H[i] + S[i] * (N - 1) for i in range(N)]
# print(penalties)
min_penalty = min(penalties)
max_penalty = max(penalties)


def can_crack(penalty):
    # penaltyを超えないためには風船 H_i を何秒までに割らなければならないかを考える
    l_sec = [(penalty - H[i]) // S[i] for i in range(N)]
    l_sec = sorted(l_sec)
    time = 0
    for sec in l_sec:
        if sec < time:
            return False
        time += 1
    return True


def bs(left, right):
    while left < right:
        mid = (left + right) // 2
        if can_crack(mid):
            right = mid
        else:
            left = mid + 1
    return right


left = min_penalty
right = max_penalty + 1
print(bs(left, right))
