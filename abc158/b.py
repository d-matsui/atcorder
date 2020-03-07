#!/usr/bin/env python3

N, A, B = map(int, input().split())

if A == 0:
    print(0)
elif B == 0:
    print(N)
elif A + B == N:
    print(A)
elif A + B > N and N >= A:
    print(A)
elif A + B > N and N < A:
    print(N)
# 8 10 4
# bbbbbbbb bbrrrr
else:
    r = int(N / (A+B))
    q = N % (A+B)
    if (q <= A):
        print(r * A + q)
    else:
        print(r * A + A)

# 8 1 4
# brrrrbrr rr

# -----
# 8 4 2
# bbbbrrbb bb

# 13 4 2
# bbbb rr bbbb rr b

# 2 4 2
# bb

# r = N / (A+B)
# q = N % (A+B)
# r * A + q
