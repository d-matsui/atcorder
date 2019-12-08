#!/usr/bin/env python

N, A, B = map(int, input().split())
# print(N, A, B)

ans = 0;
for num in range(1, N+1):
    l = []
    q, r = divmod(num, 10)
    l.append(r)
    while q != 0:
        q, r = divmod(q, 10)
        l.append(r)
    if A <= sum(l) and sum(l) <= B:
        # print(num)
        ans += num

print(ans)
