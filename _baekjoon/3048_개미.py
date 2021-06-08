# 16:17 ~ 16:33

import sys
sys.stdin = open('input.txt', 'r')


N1, N2 = map(int, input().split())
move = {}
ant1 = list(input())
ant2 = list(input())
for i in ant1:
    move[i] = 1
for i in ant2:
    move[i] = -1

order = list(reversed(ant1)) + ant2
N = N1 + N2 - 1
for _ in range(int(input())):
    i = 0
    while i < N:
        if move[order[i]] == 1 and move[order[i+1]] == -1:
            order[i], order[i+1] = order[i+1], order[i]
            i += 2
        else:
            i += 1

print(''.join(order))
