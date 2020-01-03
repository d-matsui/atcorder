#!/usr/bin/env python3

x = int(input())
# print(x)

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        # 1 is not prime
        return False

num = x
while True:
    if is_prime(num):
        print(num)
        break
    num += 1
