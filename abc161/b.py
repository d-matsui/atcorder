#!/usr/bin/env python3

n, m = map(int, input().split())
a = list(map(int, input().split()))
# print(n, m, a)

sum_vote = sum(a)
cond = (1 / (4 * m)) * sum_vote

a = sorted(a, reverse=True)

# print(a)
flag = True
for i in range(m):
    if a[i] < cond:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
