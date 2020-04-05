#!/usr/bin/env python3

n = int(input())
s = list(input())
s = [int(i) for i in s]


def is_valid(s, pin):
    i, j, k = pin
    s_tmp = s[:]
    if i not in s_tmp:
        return False
    i_idx = s_tmp.index(i)
    s_tmp = s_tmp[i_idx + 1:]
    if j not in s_tmp:
        return False
    j_idx = s_tmp.index(j)
    s_tmp = s_tmp[j_idx + 1:]
    if k not in s_tmp:
        return False
    return True


num = 10
res = 0
for i in range(num):
    for j in range(num):
        for k in range(num):
            pin = [i, j, k]
            if is_valid(s, pin):
                # print(f"{pin} is valid pin")
                res += 1

print(res)
