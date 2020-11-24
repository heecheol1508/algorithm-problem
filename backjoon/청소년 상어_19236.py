from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def init():
    global init_shark
    for i in range(4):
        row = list(map(int, input().split()))
        for j in range(4):
            fish_number = row[2 * j] - 1
            fish_direction = row[2 * j + 1] - 1
            init_board[i][j] = fish_number
            init_fish_info[fish_number] = [True, i, j, fish_direction]

    init_fish = init_board[0][0]
    init_board[0][0] = 20
    init_fish_info[init_fish][0] = False
    init_shark = [0, 0, init_fish_info[init_fish][3]]


def possible_to_move(idx1, idx2, direction):

    for ccw in range(8):
        next_direction = direction + ccw
        nxt1, nxt2 = idx1 + adj_list[next_direction][0], idx2 + adj_list[next_direction][1]
        if 0 <= nxt1 < 4 and 0 <= nxt2 < 4:
            if board[nxt1][nxt2] != 20:
                pass

    return


def time_to_move_fish():

    for k in range(16):
        alive, idx1, idx2, direction = fish_info[k]
        if alive:
            possible_to_move(idx1, idx2, direction)

    return


init_board = [[0] * 4 for _ in range(4)]
init_fish_info = [[] for _ in range(16)]
init_shark = []

adj_list = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

init()
queue = [[[], init_shark, init_board, init_fish_info]]

while queue:
    caught, shark, board, fish_info = queue.pop(0)
    break

