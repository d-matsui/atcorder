#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


a = int(input())
res = a + a ** 2 + a ** 3
print(res)
