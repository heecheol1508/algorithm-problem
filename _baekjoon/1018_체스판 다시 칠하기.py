import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

answer = 64
for i in range(N-7):
    for j in range(M-7):
        paint = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c) % 2:
                    if board[r][c] == 'W':
                        paint += 1
                else:
                    if board[r][c] == 'B':
                        paint += 1
        answer = min(answer, paint, 64-paint)

print(answer)
