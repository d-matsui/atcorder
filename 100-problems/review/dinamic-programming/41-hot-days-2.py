#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


d_days, n_kinds = map(int, input().split())

temp_list = []
for _ in range(d_days):
    temp = int(input())
    temp_list.append(temp)
# print(temp_list)

clothes_list = []
for _ in range(n_kinds):
    clothes = list(map(int, input().split()))
    clothes_list.append(clothes)
# print(clothes_list)

# dp[i+1][j] := i日目に服jを着たときの、1~i日目までに着た服の派手さの差の絶対値和の最大値
# dp[i+1][j] = max(dp[i][k] + abs(clothes_list[k] - clothes_list[j]))
# k \in {0, 1, ..., n_kinds-1} \ {j} and
# clothes_list[j][0] <= temp_list[i] <= clothes_list[j][1]
# clothes_list[k][0] <= temp_list[i-1] <= clothes_list[k][1]

dp = [[0 for j in range(n_kinds)] for i in range(d_days + 1)]

for i in range(1, d_days):
    for j in range(n_kinds):
        min_temp_j = clothes_list[j][0]
        max_temp_j = clothes_list[j][1]
        if not min_temp_j <= temp_list[i] <= max_temp_j:
            continue
        for k in range(n_kinds):
            min_temp_k = clothes_list[k][0]
            max_temp_k = clothes_list[k][1]
            if not min_temp_k <= temp_list[i-1] <= max_temp_k:
                continue
            diff = abs(clothes_list[k][2] - clothes_list[j][2])
            dp[i+1][j] = max(dp[i+1][j], dp[i][k] + diff)

# pprint(dp)
print(max(dp[d_days]))
