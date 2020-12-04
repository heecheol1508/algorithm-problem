import sys
sys.stdin = open('input.txt', 'r')


def charging(ar, ac, br, bc):
    if board[ar][ac] and board[br][bc]:
        if board[ar][ac][0] == board[br][bc][0]:
            if len(board[ar][ac]) == 1 and len(board[br][bc]) == 1:
                return board[ar][ac][0][0]
            elif len(board[ar][ac]) == 1:
                return board[ar][ac][0][0] + board[br][bc][1][0]
            elif len(board[br][bc]) == 1:
                return board[ar][ac][1][0] + board[br][bc][0][0]
            elif board[ar][ac][1][0] >= board[br][bc][1][0]:
                return board[ar][ac][1][0] + board[br][bc][0][0]
            else:
                return board[ar][ac][0][0] + board[br][bc][1][0]
        else:
            return board[ar][ac][0][0] + board[br][bc][0][0]
    elif board[ar][ac]:
        return board[ar][ac][0][0]
    elif board[br][bc]:
        return board[br][bc][0][0]
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())

    a_info = list(map(int, input().split()))
    b_info = list(map(int, input().split()))
    board = [[[] for _ in range(10)] for _ in range(10)]

    for k in range(1, A+1):
        y, x, c, p = map(int, input().split())

        for i in range(10):
            for j in range(10):
                if abs(i-x+1) + abs(j-y+1) <= c:
                    board[i][j].append((p, k))
                    board[i][j].sort(reverse=True)

    move = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
    a1, a2, b1, b2 = 0, 0, 9, 9
    answer = charging(a1, a2, b1, b2)

    for m in range(M):
        a1 += move[a_info[m]][0]
        a2 += move[a_info[m]][1]
        b1 += move[b_info[m]][0]
        b2 += move[b_info[m]][1]
        power = charging(a1, a2, b1, b2)
        answer += power

    print('#{} {}'.format(t, answer))
