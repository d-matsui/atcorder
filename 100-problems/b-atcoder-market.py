#!/usr/bin/env python3

# \sigma(|x - a_i|)が最小になるxは、a_1, a_2, ..., a_Nの中央値である。
# 移動距離の和は、\sigma(|a_i| - s) + \sigma(|b_i - a_i|) + \sigma(|t - b_i|)
# であるので、Aの中央値とBの中央値を求めて、それぞれs, tとすればよい。
# ちなみに、s, tの候補は、a_1, a_2, ..., a_N, b_1, b_2, ..., b_Nであるから、
# ここから全探索して解いても、O(n^3)で求まる。

N = int(input())
A = []
B = []
for i in range(N):
    A_i, B_i = map(int, input().split())
    A.append(A_i)
    B.append(B_i)
# print(n, a, b)

def steps(a, b, s, t):
    s_to_a = abs(a - s)
    a_to_b = abs(b - a)
    b_to_t = abs(t - b)
    return s_to_a + a_to_b + b_to_t

def median(arr):
    n = len(arr)
    arr_sorted = sorted(arr)
    if (n % 2 == 0):
        left = arr_sorted[int(n / 2) - 1]
        right = arr_sorted[int(n / 2)]
        return (left + right) / 2
    else:
        return arr_sorted[int(n / 2)]

s = int(median(A))
t = int(median(B))

res = 0
for i in range(N):
    res += steps(A[i], B[i], s, t)

print(res)

# ----- 1 <= N <= 30, 1 <= A_i < B_i <= 100のときは以下でOK
# def steps(a, b, s, t):
#     s_to_a = abs(a - s)
#     a_to_b = abs(b - a)
#     b_to_t = abs(t - b)
#     return s_to_a + a_to_b + b_to_t

# l_steps = []
# for s in range(1, 100+1):
#     for t in range(1, 100+1):
#         res = 0
#         for i in range(N):
#             a = A[i]
#             b = B[i]
#             res += steps(a, b, s, t)
#         l_steps.append(res)

# print(min(l_steps))
