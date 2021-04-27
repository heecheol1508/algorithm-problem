import sys
sys.stdin = open('input.txt', 'r')


def state(n):
    if n == 0:
        return [0]
    else:
        return [3, n, n]


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())

    board1 = [list(map(state, input().split())) for _ in range(N)]

    for h in range(K):
        if h % 2:
            N, M = N + 2, M + 2
            board2 = [[[0] for _ in range(M)] for _ in range(N)]
            for i in range(N-2):
                for j in range(M-2):
                    if board1[i][j][0] == 3:
                        if board1[i][j][1] == 1:
                            board2[i + 1][j + 1] = [2, board1[i][j][2], board1[i][j][2]]
                        else:
                            board2[i + 1][j + 1] = [3, board1[i][j][1] - 1, board1[i][j][2]]
                    elif board1[i][j][0] == 2:
                        
