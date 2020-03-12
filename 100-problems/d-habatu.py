#!/usr/bin/env python3

N, M = map(int, input().split())
friends = []
for i in range(M):
    x, y = list(map(int, input().split()))
    friends.append([x-1, y-1])

# print(N, M)
# print(rels)

groups = []
for bit in range(2 ** N):
    group = []
    # 派閥に属する人の番号のリストを求める
    for i in range(N):
        if bit & (1 << i):
            group.append(i)
    # print(f"\ngroup: {group}")
    # 派閥が作れるかどうかを判定する
    isGroup = True
    for x in group:
        for y in group:
            if x!= y and x < y:
                if [x, y] not in friends:
                    # print(f"x: {x} and y: {y} are not friend")
                    isGroup = False
                    break
        if not isGroup:
            break
    if isGroup:
        # print(f"{group} is group")
        groups.append(group)

# print(groups)
# print(list(map(lambda x: len(x), groups)))
print(max(map(lambda x: len(x), groups)))

# ----- 考えたこと -----
# 派閥: 000111
# friendsが与えられたとき、上記の派閥を作れるか。

# 作れるときってどんなときか。
# friendsに以下が含まれているとき。
# (0, 1), (0, 2), (1, 2)
# 派閥のbitに1が立っている人たち全員が知り合いであれば作れる。

# それってどうやったらわかるか。
# l_id: bitに1が立っている箇所のリストを求めて、
# 以下のループを回したあとにisGroupがTrueであれば作れる。
# isGroup = True
# for x in range(0, l_id-1):
#     for y in range(1, l_id):
#         if ![x, y] in friends:
#             isGroup = False

# l_id: bitに1が立っている箇所のリストをどうやって求めるか。
# 以下を行えばよい。
# l_id = []
# for i in range(N):
#     if bit & (1 << i):
#         l_id.append(i)
