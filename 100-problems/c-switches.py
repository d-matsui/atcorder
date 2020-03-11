#!/usr/bin/env python3

N, M = list(map(int, input().split()))
k = []
s = []
for i in range(M):
    l = list(map(int, input().split()))
    k.append(l[0])
    s.append(l[1:])
p = list(map(int, input().split()))

# print(f"N: {N}, M: {M}")
# print(f"k: {k}")
# print(f"s: {s}")
# print(f"p: {p}")

res = 0
for bit in range(2 ** N):
    # print(f"bit: {bin(bit)}")
    num_on = 0
    for i_light in range(M):
        # print(f"# check light {i_light} is on")
        count = 0
        for k_switch in range(k[i_light]):
            # s[i, k_i]番目のswitchがonかどうか
            if bit & (1 << s[i_light][k_switch]-1):
                # print(f"### switch {s[i_light][k_switch]} is on")
                count += 1
            # else:
                # print(f"### switch {s[i_light][k_switch]} is NOT on")
        # i番目のlightが点灯しているとき
        # print(f"# count % 2 == p[i]: {count%2} == {p[i_light]}")
        if count % 2 == p[i_light]:
            # print(f"## light {i_light} is on")
            num_on += 1
        # else:
            # print(f"## light {i_light} is NOT on")
    # M個のlight全てが点灯しているとき
    if num_on == M:
        # print(f"all light is on")
        res += 1

print(res)
