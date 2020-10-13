import sys
sys.stdin = open('input.txt', 'r')


def put_type_1(board, c, mark):
    for r in range(2, 6):
        if board[r][c] != 0:
            board[r-1][c] = mark
            break
    else:
        board[5][c] = mark


def put_type_2(board, c1, mark):
    c2 = c1 + 1
    for r in range(2, 6):
        if board[r][c1] != 0 or board[r][c2] != 0:
            board[r-1][c1] = board[r-1][c2] = mark
            break
    else:
        board[5][c1] = board[5][c2] = mark


def put_type_3(board, c, mark):
    for r in range(2, 6):
        if board[r][c] != 0:
            board[r-1][c] = board[r-2][c] = mark
            break
    else:
        board[5][c] = board[4][c] = mark


def check_lines(board):
    erased = 0
    for r in range(2, 6):
        if 0 not in board[r]:
            board[r] = [0, 0, 0, 0]
            erased += 1
    return erased


def down_after_scored(board):

    moved = []
    for r in range(5, -1, -1):
        for c in range(4):
            if board[r][c] and board[r][c] not in moved:
                mark = board[r][c]
                moved.append(mark)

                if r == 5:
                    continue

                if c < 3 and board[r][c+1] == mark:
                    for nr in range(r+1, 6):
                        if board[nr][c] != 0 or board[nr][c+1] != 0:
                            break
                    else:
                        nr = 6

                    if nr != r+1:
                        board[r][c], board[r][c + 1] = 0, 0
                        board[nr-1][c], board[nr-1][c+1] = mark, mark

                else:
                    for nr in range(r+1, 6):
                        if board[nr][c] != 0:
                            break
                    else:
                        nr = 6

                    if nr != r+1:
                        if r > 0 and board[r-1][c] == mark:
                            board[r][c], board[r - 1][c] = 0, 0
                            board[nr-1][c], board[nr-2][c] = mark, mark
                        else:
                            board[nr-1][c], board[r][c] = mark, 0


def down_the_lines(board):
    for _ in range(2):
        if sum(board[1]) != 0:
            board.pop()
            board.insert(0, [0, 0, 0, 0])


N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

score = 0

for m in range(1, N+1):
    t, x, y = map(int, input().split())
    if t == 1:
        put_type_1(green, y, m)
        put_type_1(blue, x, m)
    elif t == 2:
        put_type_2(green, y, m)
        put_type_3(blue, x, m)
    else:
        put_type_3(green, y, m)
        put_type_2(blue, x, m)

    while True:
        check_green = check_lines(green)
        if check_green:
            score += check_green
            down_after_scored(green)
        else:
            break

    while True:
        check_blue = check_lines(blue)
        if check_blue:
            score += check_blue
            down_after_scored(blue)
        else:
            break

    down_the_lines(green)
    down_the_lines(blue)

cnt = 0
for i in range(6):
    for j in range(4):
        if green[i][j] > 0:
            cnt += 1
        if blue[i][j] > 0:
            cnt += 1

print(score)
print(cnt)
