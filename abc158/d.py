#!/usr/bin/env python3

from collections import deque

S = str(input())
Q = int(input())
# print(S, Q)

is_reverse = False


for i in range(Q):
    query = list(input().split())
    # print(query)
    if int(query[0]) == 1:
        # print("reverse")
        # Sを反転
        # S_copy = S_copy[::-1]
        is_reverse = not is_reverse
    else:
        if int(query[1]) == 1:
            # Sの先頭にC_iを追加
            # print("prepend C_i")
            if is_reverse:
                S_copy = S_copy + query[2]
            else:
                S_copy = query[2] + S_copy
        else:
            # Sの末尾にC_iを追加
            # print("append C_i")
            if is_reverse:
                S_copy = query[2] + S_copy
            else:
                S_copy = S_copy + query[2]

if is_reverse:
    print(S_copy[::-1])
else:
    print(S_copy)
