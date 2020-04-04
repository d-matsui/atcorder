#!/usr/bin/env python3

n, k = map(int, input().split())

if n == 0 or n == k:
    print(0)
elif k == 1:
    print(0)
else:
    if n > k:
        r = n % k
        if r == 0:
            print(0)
        else:
            n_1 = abs(r - k)
            n_2 = abs(n_1 - k)
            print(min(n_1, n_2))
    else:
        n_1 = abs(n - k)
        n_2 = abs(n_1 - k)
        print(min(n_1, n_2))
