import sys
sys.stdin = open('input.txt', 'r')


def biggest_size(board, x, y):
    for size in range(5, 0, -1):
        found_size = True
        for nx in range(x, x + size):
            if nx >= 10:
                found_size = False
                break
            for ny in range(y, y + size):
                if ny < 10 and board[nx][ny] == 1:
                    continue
                else:
                    found_size = False
                    break
        if found_size:
            return size


def is_possible_to_fix(x, y, size):
    if x > 0:
        for ny in range(y, y + size):
            if board_init[x-1][ny] == 1:
                return False
    if y > 0:
        for nx in range(x, x + size):
            if board_init[nx][y-1] == 1:
                return False
    if y + size < 10:
        for nx in range(x, x + size):
            if board_init[nx][y+size] == 1:
                return False

    if x + size < 10:
        for ny in range(y, y + size):
            if board_init[x+size][ny] == 1:
                return False

    return True


def recursion(board, r, cnt, unused):
    global paper_needed_minimum

    if cnt >= paper_needed_minimum:
        return

    for x in range(r, 10):
        for y in range(10):
            if board[x][y] == 1:
                size = board_for_size[x][y]

                for size_temp in range(size, 0, -1):
                    if unused[size_temp] > 0:
                        temp_board = [row[:] for row in board]
                        flag = False
                        for nx in range(x, x + size_temp):
                            for ny in range(y, y + size_temp):
                                if temp_board[nx][ny] == 1:
                                    temp_board[nx][ny] = 0
                                else:
                                    flag = True
                                    break
                            if flag:
                                break
                        if flag:
                            continue
                        temp_unused = unused[:]
                        temp_unused[size_temp] -= 1
                        recursion(temp_board, x, cnt + 1, temp_unused)
                return

    if cnt < paper_needed_minimum:
        print(cnt, unused)
        paper_needed_minimum = cnt
    return


board_init = [list(map(int, input().split())) for _ in range(10)]
board_for_size = [[0] * 10 for _ in range(10)]
paper_left = [0, 5, 5, 5, 5, 5]

# greedy
cnt_paper_for_greedy = 0
for i in range(10):
    for j in range(10):
        if board_init[i][j] == 1:
            paper_size = biggest_size(board_init, i, j)
            board_for_size[i][j] = paper_size

            if paper_left[paper_size] > 0 and is_possible_to_fix(i, j, paper_size):
                paper_left[paper_size] -= 1
                cnt_paper_for_greedy += 1
                for ni in range(i, i + paper_size):
                    for nj in range(j, j + paper_size):
                        board_init[ni][nj] = 0

# brute force, recursion
paper_needed_minimum = 100
recursion(board_init, 0, 0, paper_left)

if paper_needed_minimum == 100:
    print(-1)
else:
    print(cnt_paper_for_greedy + paper_needed_minimum)
