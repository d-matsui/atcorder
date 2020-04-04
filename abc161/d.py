#!/usr/bin/env python3

from collections import deque

k = int(input())

que = deque(reversed([i for i in range(1, 10)]))

x = -1
for _ in range(k):
    # print(f"loop: {_}")
    # print(f"que: {que}")
    x = que.pop()
    # print(f"x: {x}\n")
    r_10 = x % 10
    if r_10 == 0:
        # 10, 100, 1000, ...
        que.appendleft(x * 10)
        que.appendleft(x * 10 + 1)
    elif r_10 == 9:
        # 9, 99, 989, 999, ...
        que.appendleft(x * 10 + x % 10 - 1)
        que.appendleft(x * 10 + x % 10)
    else:
        # 1, 2, ..., 8, 11, 12, 21, 22, 23, ...
        que.appendleft(x * 10 + x % 10 - 1)
        que.appendleft(x * 10 + x % 10)
        que.appendleft(x * 10 + x % 10 + 1)

print(x)
