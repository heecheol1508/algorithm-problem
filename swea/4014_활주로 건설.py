import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    # 가로
    for i in range(N):
        height = board[i][0]
        cnt = 1
        downhill = False
        is_possible = True
        for j in range(1, N):
            if downhill:
                if board[i][j] == height:
                    cnt += 1
                    if cnt >= X:
                        downhill = False
                        cnt = 0
                else:
                    is_possible = False
                    break

            elif board[i][j] == height:
                cnt += 1

            elif board[i][j] == height + 1:
                if cnt >= X:
                    height = board[i][j]
                    cnt = 1
                else:
                    is_possible = False
                    break

            elif board[i][j] == height - 1:
                downhill = True
                height = board[i][j]
                cnt = 1

            else:
                is_possible = False
                break

        if is_possible and downhill is False:
            answer += 1

    # 세로
    for j in range(N):
        height = board[0][j]
        cnt = 1
        downhill = False
        is_possible = True
        for i in range(1, N):
            if downhill:
                if board[i][j] == height:
                    cnt += 1
                    if cnt >= X:
                        downhill = False
                        cnt = 0
                else:
                    is_possible = False
                    break

            elif board[i][j] == height:
                cnt += 1

            elif board[i][j] == height + 1:
                if cnt >= X:
                    height = board[i][j]
                    cnt = 1
                else:
                    is_possible = False
                    break

            elif board[i][j] == height - 1:
                downhill = True
                height = board[i][j]
                cnt = 1

            else:
                is_possible = False
                break

        if is_possible and downhill is False:
            answer += 1

    print('#{} {}'.format(t, answer))
