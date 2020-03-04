#!/usr/bin/env python3

N = int(input())
# print(N)

result = 0
for num in range(1, N+1):
    if num % 2 == 1:
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count == 8:
            result += 1

print(result)
