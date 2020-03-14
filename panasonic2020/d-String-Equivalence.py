#!/usr/bin/env python3

import string
import itertools

N = int(input())

ascii_lower = string.ascii_lowercase
str_combinations = list(map(list, itertools.combinations_with_replacement(ascii_lower, N)))
# print(str_combinations)

def is_same_type(s, t):
    n = len(s)
    flag = True
    for i in range(n):
        for j in range(n):
            if not (s[i] == s[j] and t[i] == t[j]):
                flag = False
    if flag:
        return True

    for i in range(n):
        for j in range(n):
            if not (s[i] != s[j] and t[i] != t[j]):
                flag = False
    if flag:
        return True

def is_standard_type(s, t_list):
    for t in t_list:
        if s > t:
            return False
    return True

ans = []
for s in str_combinations:
    t_list = []
    s_str = "".join(s)
    for t in str_combinations:
        t_str = "".join(t)
        if is_same_type(s_str, t_str):
            t_list.append(t_str)
    if is_standard_type(s_str, t_list):
        ans.append(s_str)

for i in range(len(ans)):
    print(ans[i])
