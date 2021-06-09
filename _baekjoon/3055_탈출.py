import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

hedgehog = deque()
water = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == '.' or board[i][j] == 'X':
            continue
        elif board[i][j] == '*':
            water.append((i, j))
        elif board[i][j] == 'S':
            hedgehog.append((i, j))

flag = False
minute = 0
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while hedgehog:
    minute += 1
    for _ in range(len(water)):
        idx1, idx2 = water.popleft()
        for di, dj in adj:
            nxt1, nxt2 = idx1 + di, idx2 + dj
            if 0 <= nxt1 < R and 0 <= nxt2 < C:
                if board[nxt1][nxt2] == '.' or board[nxt1][nxt2] == 'S':
                    board[nxt1][nxt2] = '*'
                    water.append((nxt1, nxt2))
    for _ in range(len(hedgehog)):
        idx1, idx2 = hedgehog.popleft()
        for di, dj in adj:
            nxt1, nxt2 = idx1 + di, idx2 + dj
            if 0 <= nxt1 < R and 0 <= nxt2 < C:
                if board[nxt1][nxt2] == '.':
                    board[nxt1][nxt2] = 'S'
                    hedgehog.append((nxt1, nxt2))
                elif board[nxt1][nxt2] == 'D':
                    flag = True
                    break
        if flag:
            break
    if flag:
        break
if flag:
    print(minute)
else:
    print('KAKTUS')
