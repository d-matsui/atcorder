#!/usr/bin/env python3

m = int(input())
n = int(input())

field = []
for _ in range(n):
    line = list(map(int, input().split()))
    field.append(line)

# print(n, m)
# print(*field)


def adj(i, j):
    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    if i == 0:
        if j == 0:
            return [down, right]
        elif j == m - 1:
            return [down, left]
        else:
            return [down, left, right]
    elif i == n - 1:
        if j == 0:
            return [up, right]
        elif j == m - 1:
            return [up, left]
        else:
            return [up, left, right]
    else:
        if j == 0:
            return [up, down, right]
        elif j == m - 1:
            return [up, down, left]
        else:
            return [up, down, left, right]


def dfs(field, i, j, count):
    # print(f"i, j: {i}, {j}")
    global max_count
    count += 1
    field[i][j] = 0
    for i_next, j_next in adj(i, j):
        if field[i_next][j_next] == 1:
            dfs(field, i_next, j_next, count)
    field[i][j] = 1

    if all([field[x][y] == 0 for x, y in adj(i, j)]):
        # print(f"stopped: {i}, {j}")
        # print(f"count: {count}")
        if count > max_count:
            max_count = count


max_count = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            dfs(field, i, j, 0)

print(max_count)
