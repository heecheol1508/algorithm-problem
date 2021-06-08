# 16:33

import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [list(input()) for _ in range(N)]

answer = 1


def check():
    temp = 0
    for r in range(N):
        cnt = 1
        for c in range(1, N):
            if board[r][c] == board[r][c-1]:
                cnt += 1
            else:
                temp = max(temp, cnt)
                cnt = 1
        temp = max(temp, cnt)

    for c in range(N):
        cnt = 1
        for r in range(1, N):
            if board[r][c] == board[r-1][c]:
                cnt += 1
            else:
                temp = max(temp, cnt)
                cnt = 1
        temp = max(temp, cnt)

    return temp


for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

for i in range(N-1):
    for j in range(N):
        if board[i][j] != board[i + 1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)
