#!/usr/bin/env python3

# a 回目、b 回目を考えたとき、a mod K と b mod K の値が異なれば、a, b それぞれの回で独立に手を選べる。
# mod K の値に応じて、N 回のジャンケンを K 個のグループに分けたとき、各グループに対して、最大何点取れるかを考えればよい。
# あるグループで最大何点取れるかは、前回の手を覚えておきながら DP or 貪欲法で求めればよい。

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = str(input())
# print(n, k, r, s, p, t)

t_list = list(t)
groups = [[] for i in range(k)]
for i in range(len(t_list)):
    mod = i % k
    groups[mod].append(t_list[i])
# print(groups)

def score(my_hand, hand):
    if my_hand == 'r' and hand == 's':
        return r
    elif my_hand == 's' and hand == 'p':
        return s
    elif my_hand == 'p' and hand == 'r':
        return p
    return 0

def get_win_hand(hand):
    if hand == 'r':
        return 'p'
    elif hand == 's':
        return 'r'
    else:
        return 's'

result = 0
# for each group
for i in range(k):
    hands = groups[i]
    # for each hand in a group
    for j in range(len(hands)):
        hand = hands[j]
        win_hand = get_win_hand(hand)
        if j == 0:
            my_hand = win_hand
            result += score(my_hand, hand)
            my_hand_prev = my_hand
        else:
            candidates = ['r', 's', 'p']
            candidates.remove(my_hand_prev)
            if win_hand == my_hand_prev:
                if j == len(hands) - 1:
                    candidates.pop()
                    my_hand = candidates[0]
                else:
                    hand_next = hands[j+1]
                    win_hand_next = get_win_hand(hand_next)
                    if win_hand_next == my_hand_prev:
                        candidates.pop()
                    else:
                        candidates.remove(win_hand_next)
                my_hand = candidates[0]
                result += score(my_hand, hand)
                my_hand_prev = my_hand
            else:
                my_hand = win_hand
                result += score(my_hand, hand)
                my_hand_prev = my_hand

print(result)
