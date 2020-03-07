#!/usr/bin/env python3

from collections import deque

S = str(input())
Q = int(input())
# print(S, Q)

is_reverse = False

d = deque()
d.append(S)
# print(d)

for i in range(Q):
    query = list(input().split())
    # print(query)
    if int(query[0]) == 1:
        # print("reverse")
        # Sを反転
        is_reverse = not is_reverse
    else:
        if int(query[1]) == 1:
            # Sの先頭にC_iを追加
            if is_reverse:
                d.append(query[2])
            else:
                d.appendleft(query[2])
        else:
            # Sの末尾にC_iを追加
            if is_reverse:
                d.appendleft(query[2])
            else:
                d.append(query[2])

if is_reverse:
    print("".join(d)[::-1])
else:
    print("".join(d))
