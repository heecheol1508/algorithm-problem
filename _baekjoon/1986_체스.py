import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

board = [[0] * M for _ in range(N)]
Q = []
K = []
P = []

for i in range(queen[0]):
    x = queen[2*i+1] - 1
    y = queen[2*i+2] - 1
    board[x][y] = 1
    Q.append((x, y))

for i in range(knight[0]):
    x = knight[2*i+1] - 1
    y = knight[2*i+2] - 1
    board[x][y] = 1
    K.append((x, y))

for i in range(pawn[0]):
    x = pawn[2*i+1] - 1
    y = pawn[2*i+2] - 1
    board[x][y] = 1
    P.append((x, y))

for (i, j) in Q:
    k = 1
    while i - k >= 0 and board[i - k][j] != 1:
        board[i - k][j] = 2
        k += 1
    k = 1
    while i - k >= 0 and j + k < M and board[i - k][j + k] != 1:
        board[i - k][j + k] = 2
        k += 1
    k = 1
    while j + k < M and board[i][j + k] != 1:
        board[i][j + k] = 2
        k += 1
    k = 1
    while j + k < M and i + k < N and board[i + k][j + k] != 1:
        board[i + k][j + k] = 2
        k += 1
    k = 1
    while i + k < N and board[i + k][j] != 1:
        board[i + k][j] = 2
        k += 1
    k = 1
    while i + k < N and j - k >= 0 and board[i + k][j - k] != 1:
        board[i + k][j - k] = 2
        k += 1
    k = 1
    while j - k >= 0 and board[i][j - k] != 1:
        board[i][j - k] = 2
        k += 1
    k = 1
    while j - k >= 0 and i - k >= 0 and board[i - k][j - k] != 1:
        board[i - k][j - k] = 2
        k += 1

moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
for (i, j) in K:
    for (di, dj) in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 1:
            board[ni][nj] = 2

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            answer += 1

for row in board:
    print(row)
print(answer)
