#!/usr/bin/env python

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

N = int(input())
t_list = [0]
x_list = [0]
y_list = [0]
for i in range(N):
    t, x, y = map(int, input().split())
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)
# print(t_list)
# print(x_list)
# print(y_list)

is_reachable = False
for i in range(N):
    # t = 0, (x, y) = (0, 0)
    num_steps = t_list[i+1] - t_list[i]
    x_dist = abs(x_list[i+1] - x_list[i])
    y_dist = abs(y_list[i+1] - y_list[i])
    dist = x_dist + y_dist
    # print('i:', i, 'num_steps:', num_steps, 'distance:', dist)
    # print(num_steps >= dist and is_even(num_steps) == is_even(dist))

    if num_steps >= dist and is_even(num_steps) == is_even(dist):
        is_reachable = True
    else:
        is_reachable = False
        break

if is_reachable:
    print('Yes')
else:
    print('No')
