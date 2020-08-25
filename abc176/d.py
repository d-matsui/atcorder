#!/usr/bin/env python3

from collections import deque

INF = 10 ** 12


H, W = map(int, input().split())
s_i, s_j = map(lambda x: int(x) - 1, input().split())
t_i, t_j = map(lambda x: int(x) - 1, input().split())
field = [input() for _ in range(H)]

# 1. bfs でワープなしで到達できるマスを探索
# 2. 1 で見つかったマスから一回ワープして到達できるマスを探索
# 3. 1, 2 を繰り返す


walk = [(1, 0), (0, 1), (-1, 0), (0, -1)]
warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + walk]

warp_times = [[INF for j in range(W)] for i in range(H)]
que = deque()

warp_times[s_i][s_j] = 0
que.append((s_i, s_j, 0))

while que:
    i, j, times = que.popleft()
    # ワープ無しで到達できるマスの探索
    for di, dj in walk:
        i_adj, j_adj = i + di, j + dj
        if 0 <= i_adj < H and 0 <= j_adj < W and field[i_adj][j_adj] == '.':
            if warp_times[i_adj][j_adj] > times:
                warp_times[i_adj][j_adj] = times
                que.appendleft((i_adj, j_adj, times))

    # ワープ有りで到達できるマスの探索
    for di, dj in warp:
        i_adj, j_adj = i + di, j + dj
        if 0 <= i_adj < H and 0 <= j_adj < W and field[i_adj][j_adj] == '.':
            if warp_times[i_adj][j_adj] > times + 1:
                warp_times[i_adj][j_adj] = times + 1
                # ワープ無しで到達できるマスを探索しきった後に探索するため、単に append
                que.append((i_adj, j_adj, times + 1))

ans = warp_times[t_i][t_j] if warp_times[t_i][t_j] < INF else '-1'
print(ans)
