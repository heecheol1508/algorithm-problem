import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
nxt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in range(1, T+1):
    N, M, K = map(int, input().split())

    microbe = {}
    for k in range(1, K+1):
        a, b, c, d = map(int, input().split())
        microbe[k] = [True, a, b, c, d-1]

    for _ in range(M):
        board = [[[] for ___ in range(N)] for __ in range(N)]

        for k in range(1, K+1):
            if microbe[k][0]:
                alive, idx1, idx2, number, direction = microbe[k]
                nxt1, nxt2 = idx1 + nxt[direction][0], idx2 + nxt[direction][1]

                if nxt1 == 0 or nxt1 == N-1 or nxt2 == 0 or nxt2 == N-1:
                    number //= 2
                    if number == 0:
                        microbe[k][0] = False
                        continue
                    else:
                        if direction % 2:
                            direction -= 1
                        else:
                            direction += 1
                board[nxt1][nxt2].append([number, k])
                microbe[k] = [True, nxt1, nxt2, number, direction]

        for i in range(N):
            for j in range(N):
                if len(board[i][j]) > 1:
                    board[i][j].sort(reverse=True)
                    a = board[i][j][0][1]
                    for b in range(1, len(board[i][j])):
                        c = board[i][j][b][1]
                        microbe[a][3] += microbe[c][3]
                        microbe[c][0] = False

    answer = 0
    for k in range(1, K+1):
        if microbe[k][0]:
            answer += microbe[k][3]

    print('#{} {}'.format(t, answer))
