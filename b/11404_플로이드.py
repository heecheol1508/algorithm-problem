import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
inf = float('inf')
board = [[inf] * N for _ in range(N)]

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if c < board[a-1][b-1]:
        board[a-1][b-1] = c

for k in range(N):
    for i in range(N):
        if board[i][k] == inf:
            continue
        for j in range(N):
            if i == j or j == k:
                continue
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(N):
    for j in range(N):
        if board[i][j] == inf:
            board[i][j] = 0

for r in range(N):
    row = ' '.join(list(map(str, board[r])))
    print(row)


