#!/usr/bin/env python3

S = str(input())
# print(S)

def is_ATGC(char):
    if char == "A" or char == "C" or char == "G" or char == "T":
        return True
    return False

def is_ATGC_str(s):
    is_ATGC_str = True
    for char in s:
        if not is_ATGC(char):
            is_ATGC_str = False
    return is_ATGC_str

len_max = 0
for start in range(len(S)):
    for end in range(start+1, len(S)+1):
        # print(start, end)
        # print(S[start:end])
        s = S[start:end]
        if is_ATGC_str(s) and len(s) > len_max:
            len_max = len(s)

print(len_max)
