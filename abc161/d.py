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
    if x % 10 != 0:
        que.appendleft(x * 10 + x % 10 - 1)
    que.appendleft(x * 10 + x % 10)
    if x % 10 != 9:
        que.appendleft(x * 10 + x % 10 + 1)

print(x)
