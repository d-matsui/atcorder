#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


K = int(input())

# 解法1
# 数列 s は、s[1] = 7, s[i+1] = s[i] * 10 + 7 の漸化式で与えられる
# 特性方程式 α = α * 10 + 7 を考えると、α = -7/9 より、
# s[i+1] + 7/9 = 10 * (s[i] + 7/9) となる
# つまり、s[i] + 7/9 = 10^(i-1) * (7 + 7/9)
# <=> s[i] = 10^(i-1) * 70/9 - 7/9
# <=> s[i] = 7/9 * (10^i - 1)
# よって、7/9 * (10^i - 1) % K == 0 となるような最小の正の整数 i を求めれば良いことになる
# K と 10 が互いに素でない場合は答えが存在しないことに注意

# 解法2
# s[i] = s[i-1] * 10 + 7 より、s[i] % K = (s[i-1] * 10 + 7) % K (ただし、s[0] = 0)
# <=> s[i] % K = s[i-1] * 10 % K + 7 % K
# K と 10 が互いに素でない場合は答えが存在しないことに注意

if K % 2 == 0 or K % 5 == 0:
    print(-1)
else:
    i = 1
    s_i = 0
    while True:
        s_i = (s_i * 10 + 7) % K
        if s_i == 0:
            print(i)
            break
        i += 1
