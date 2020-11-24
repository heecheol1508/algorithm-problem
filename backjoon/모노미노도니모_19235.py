import sys
sys.stdin = open('input.txt', 'r')


green_board = [[0] * 4 for _ in range(6)]
blue_board = [[0] * 4 for _ in range(6)]


def stack_green(t, x, y):
    if t == 1:
        block_g = [(1, y)]
    elif t == 2:
        block_g = [(1, y), (1, y+1)]
    else:
        block_g = [(1, y), (0, y)]

    flag = False
    for k in range(1, 5):

        for i, j in block_g:
            if green_board[i-k][j] != 0:
                flag = True
                break
        if flag:
            for i, j in block_g:
                green_board[i-k-1][j] = 1
            break
    else:
        for i, j in block_g:
            green_board[i+4][j] = 1

    return


def stack_blue(t, x, y):
    if t == 1:
        block_b = [(1, x)]
    elif t == 2:
        block_b = [(1, x), (0, x)]
    else:
        block_b = [(1, x), (1, x+1)]

    flag = False
    for k in range(1, 5):

        for i, j in block_b:
            if blue_board[i-k][j] != 0:
                flag = True
                break
        if flag:
            for i, j in block_b:
                blue_board[i-k-1][j] = 1
            break
    else:
        for i, j in block_b:
            blue_board[i+4][j] = 1

    return


def delete_green_line():
    line = 0
    for row in range(2, 6):
        if sum(green_board[row]) == 4:
            green_board[row] = [0, 0, 0, 0]
            line += 1
    return line


def arrange_green():
    


total = 0
N = int(input())
for _ in range(N):
    block_type, x_idx, y_idx = map(int, input().split())
    stack_green(block_type, x_idx, y_idx)
    deleted = delete_green_line()
    if deleted > 0:
        total += deleted


