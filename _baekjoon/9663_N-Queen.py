import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [[0] * N for _ in range(N)]


def recursion(i, board_in):
    global answer
    if i == N:
        answer += 1
        return

    for j in range(N):
        if board_in[i][j] == 0:
            board_out = [row[:] for row in board_in]
            for a in range(i+1, N):
                if board_out[a][j] == 0:
                    board_out[a][j] = 1

                tj = a-i+j
                if 0 <= tj < N and board_out[a][tj] is 0:
                    board_out[a][tj] = 1

                tj = i+j-a
                if 0 <= tj < N and board_out[a][tj] is 0:
                    board_out[a][tj] = 1

            recursion(i+1, board_out)


answer = 0
recursion(0, board)
print(answer)
