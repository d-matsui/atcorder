#!/usr/bin/env python3

n = int(input())

ans = [0]
for i in range(1, n + 1):
    if i % 3 == 0 and 1 % 5 == 0:
        fizzbuzz = 0
    elif i % 3 == 0:
        fizzbuzz = 0
    elif i % 5 == 0:
        fizzbuzz = 0
    else:
        ans.append(i)

print(sum(ans))
