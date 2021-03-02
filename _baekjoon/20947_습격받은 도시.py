import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            # left
            for b in range(j-1, -1, -1):
                if board[i][b] == 'O' or board[i][b] == 'X':
                    break
                elif board[i][b] == '.':
                    board[i][b] = 'B'
            # right
            for b in range(j+1, N):
                if board[i][b] == 'O' or board[i][b] == 'X':
                    break
                elif board[i][b] == '.':
                    board[i][b] = 'B'
            # up
            for a in range(i-1, -1, -1):
                if board[a][j] == 'O' or board[a][j] == 'X':
                    break
                elif board[a][j] == '.':
                    board[a][j] = 'B'
            # down
            for a in range(i + 1, N):
                if board[a][j] == 'O' or board[a][j] == 'X':
                    break
                elif board[a][j] == '.':
                    board[a][j] = 'B'

for i in range(N):
    for j in range(N):
        if board[i][j] == 'O':
            # left
            for b in range(j - 1, -1, -1):
                if board[i][b] == 'O' or board[i][b] == 'X':
                    break
                elif board[i][b] == 'B':
                    board[i][b] = '.'
            # right
            for b in range(j + 1, N):
                if board[i][b] == 'O' or board[i][b] == 'X':
                    break
                elif board[i][b] == 'B':
                    board[i][b] = '.'
            # up
            for a in range(i - 1, -1, -1):
                if board[a][j] == 'O' or board[a][j] == 'X':
                    break
                elif board[a][j] == 'B':
                    board[a][j] = '.'
            # down
            for a in range(i + 1, N):
                if board[a][j] == 'O' or board[a][j] == 'X':
                    break
                elif board[a][j] == 'B':
                    board[a][j] = '.'


for row in board:
    print(''.join(row))
