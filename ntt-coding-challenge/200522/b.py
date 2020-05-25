#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
orders = list(input())
# print(orders)

posit = [0, 0]
direction = 'north'


def forward(posit, direction):
    posit_next = posit
    if direction == 'north':
        posit_next[1] = posit[1] + 1
    elif direction == 'east':
        posit_next[0] = posit[0] + 1
    elif direction == 'south':
        posit_next[1] = posit[1] - 1
    else:
        posit_next[0] = posit[0] - 1
    return posit_next


def back(posit, direction):
    posit_next = posit
    if direction == 'north':
        posit_next[1] = posit[1] - 1
    elif direction == 'east':
        posit_next[0] = posit[0] - 1
    elif direction == 'south':
        posit_next[1] = posit[1] + 1
    else:
        posit_next[0] = posit[0] + 1
    return posit_next


def right(direction):
    if direction == 'north':
        return 'east'
    elif direction == 'east':
        return 'south'
    elif direction == 'south':
        return 'west'
    return 'north'


def left(direction):
    if direction == 'north':
        return 'west'
    elif direction == 'east':
        return 'north'
    elif direction == 'south':
        return 'east'
    return 'south'


def move(posit, direction, order):
    if order == 'F':
        return forward(posit, direction)
    return back(posit, direction)


def change_direction(direction, order):
    if order == 'R':
        return right(direction)
    return left(direction)


energy = 10 ** 6
skip = False
for i in range(n):
    if energy <= 0:
        break
    if skip:
        skip = False
        continue
    if orders[i].isdecimal():
        loop = int(orders[i])
        order = orders[i + 1]
        skip = True
        for _ in range(loop):
            if energy <= 0:
                break
            if order == 'F' or order == 'B':
                posit = move(posit, direction, order)
            else:
                direction = change_direction(direction, order)
            energy -= 1
    else:
        order = orders[i]
        if order == 'F' or order == 'B':
            posit = move(posit, direction, order)
        else:
            direction = change_direction(direction, order)
        energy -= 1

print(f'{posit[0]} {posit[1]}')
