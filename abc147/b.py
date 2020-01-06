#!/usr/bin/env python3

s = list(input())
len_s = len(s)

count = 0
for i in range(len_s):
    if s[i] != s[len_s - 1 - i]:
        # print(s[i], s[len_s - 1 - i])
        s[len_s - 1 - i] = s[i]
        count += 1

print(count)
