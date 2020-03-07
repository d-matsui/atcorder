#!/usr/bin/env python3

import time
from collections import deque

s = "a"
t = time.time()
for i in range(200000):
    s = s + "b"
print(time.time() - t)

s = "a"
t = time.time()
for i in range(200000):
    s = "b" + s
print(time.time() - t)

s = deque()
s.append("a")
t = time.time()
for i in range(200000):
    s.append("b")
print(time.time() - t)

s = deque()
s.append("a")
t = time.time()
for i in range(200000):
    s.appendleft("b")
print(time.time() - t)
