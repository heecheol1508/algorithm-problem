# 14:49 ~ 15:15
import itertools

import sys
sys.stdin = open('input.txt', 'r')


words = []
init = {}
for _ in range(6):
    w = input()
    words.append(w)
    if init.get(w) is None:
        init[w] = 1
    else:
        init[w] += 1

answer = []
for rows in itertools.permutations(words, 3):
    temp = init.copy()
    for w in rows:
        temp[w] -= 1
    for i in range(3):
        w = rows[0][i] + rows[1][i] + rows[2][i]
        if temp.get(w) is None or temp[w] == 0:
            break
        else:
            temp[w] -= 1
    else:
        answer.append(rows)

if answer:
    print('\n'.join(min(answer)))
else:
    print(0)
