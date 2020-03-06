#!/usr/bin/env python3

import itertools

N = int(input())
S = str(input())

# 暗証番号Vを000から999まで決め打ちすると、次の問題を1000回解けば良いことになる。
# SからN-3桁を消して、Vを作ることができるか。
# この問題は貪欲法で解くことができる。
# - 1. S_i = V_1であるようなiのうち、最小のiをp_1とする。そのようなiが存在しなければ、Vを作ることはできない。
# - 2. S_i = V_2であるようなiのうち、p_1より大きい、かつ最も小さいiをp_2とする。そのようなiが存在しなければ、Vを作ることはできない。
# - 3. S_i = V_3であるようなiのうち、p_2より大きい、かつ最も小さいiをp_3とする。そのようなiが存在しなければ、Vを作ることはできない。
# e.g., S = 869120, V = 812
# - V_1 = 8より、p_1 = 0
# - V_2 = 1, p_1 = 0より、p_2 = 3
# - V_3 = 2, p_2 = 3より、p_3 = 4

def can_make_pw(S, password):
    # step1
    v1 = password[0]
    p1 = S.find(v1)
    if p1 == -1:
        return False
    # step2
    v2 = password[1]
    p2 = S.find(v2, p1+1)
    if p2 == -1:
        return False
    # step3
    v3 = password[2]
    p3 = S.find(v3, p2+1)
    if p3 == -1:
        return False
    return True

passwords = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            password = str(i) + str(j) + str(k)
            passwords.append(password)
# print(passwords)

count = 0
for password in passwords:
    if can_make_pw(S, password):
        # print(f"You can make {password} from {S}")
        count += 1

print(count)

# 全探索はTLE
# l_pw = []
# if N-3 == 1:
#     for i in range(N):
#         l_S = list(S)
#         l_S.pop(i)
#         l_pw.append(','.join(l_S))
# else:
#     combs = list(itertools.combinations(range(N), N-3))
#     for comb in combs:
#         l_S = list(S)
#         for i in sorted(comb, reverse=True):
#             l_S.pop(i)
#         l_pw.append(','.join(l_S))
# print(len(set(l_pw)))
