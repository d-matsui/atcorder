#!/usr/bin/env python

S = input()
S_copy = S
T = []
words = ['dream', 'dreamer', 'erase', 'eraser']

while True:
    match = False
    word_matched = ''
    # check if S_copy ends with word in words
    for word in words:
        if S_copy.endswith(word):
            match = True
            # print('S_copy is', f'{S_copy}')
            # print('ends with', f'{word}')
            if len(word) > len(word_matched):
                # print('this word is longer than previous word_matched')
                # print('word:', f'{word}')
                # print('previous word_matched:', f'{word_matched}')
                word_matched = word

    if match:
        T.insert(0, word_matched)
        # ends with dreamer
        # erasedreamer => erase
        S_copy = S_copy[:-len(word_matched)]
    else:
        break

# print(S)
# print(''.join(T))
if S == ''.join(T):
    print('YES')
else:
    print('NO')
