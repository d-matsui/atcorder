#!/usr/bin/env python

n = input()
a = list(map(int, input().split()))
# print(n)
# print(a)

alice = []
bob = []
a_sorted = sorted(a)
# print(a_sorted)

while len(a_sorted) != 0:
    max = a_sorted.pop()
    # print(max)
    alice.append(max)
    if(len(a_sorted) != 0):
        max = a_sorted.pop()
        bob.append(max)

# print(alice)
# print(bob)
print(sum(alice) - sum(bob))
