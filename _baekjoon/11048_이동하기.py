import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i > 0:
            if j > 0:
                board[i][j] += max(board[i-1][j], board[i][j-1])
            else:
                board[i][j] += board[i-1][j]
        else:
            if j > 0:
                board[i][j] += board[i][j-1]

print(board[-1][-1])
