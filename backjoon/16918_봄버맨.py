import sys
sys.stdin = open('input.txt', 'r')


R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]

if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
elif N == 1:
    for row in board:
        print(''.join(row))
else:
    bomb = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb.append((i, j))
            else:
                board[i][j] = 'O'

    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for _ in range(len(bomb)):
        idx1, idx2 = bomb.pop()
        board[idx1][idx2] = '.'
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < R and 0 <= nxt2 < C:
                board[nxt1][nxt2] = '.'

    state = (N - 2) % 4
    if state == 1:
        for row in board:
            print(''.join(row))
    else:
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    bomb.append((i, j))
                else:
                    board[i][j] = 'O'

        for _ in range(len(bomb)):
            idx1, idx2 = bomb.pop()
            board[idx1][idx2] = '.'
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < R and 0 <= nxt2 < C:
                    board[nxt1][nxt2] = '.'

        for row in board:
            print(''.join(row))
