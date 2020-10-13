# 11:28
import sys
sys.stdin = open('input.txt', 'r')
import copy


def fish_move(board_in, fish_info):
    for number_of_fish in range(1, 17):
        if fish_info[number_of_fish][0] == -1:
            continue
        else:
            idx1, idx2, current_direction = fish_info[number_of_fish]
            for k in range(8):
                next_direction = (current_direction + k - 1) % 8 + 1
                nxt1, nxt2 = idx1 + adj_list[next_direction][0], idx2 + adj_list[next_direction][1]
                if 0 <= nxt1 < 4 and 0 <= nxt2 < 4:
                    if board_in[nxt1][nxt2] > 0:        # other fish
                        number_of_fish_near = board_in[nxt1][nxt2]
                        fish_info[number_of_fish_near][0], fish_info[number_of_fish_near][1] = idx1, idx2
                        fish_info[number_of_fish] = [nxt1, nxt2, next_direction]
                        board_in[nxt1][nxt2], board_in[idx1][idx2] = number_of_fish, number_of_fish_near
                        break
                    elif board_in[nxt1][nxt2] == 0:     # shark
                        continue
                    else:                               # blank
                        board_in[nxt1][nxt2], board_in[idx1][idx2] = number_of_fish, -1
                        fish_info[number_of_fish] = [nxt1, nxt2, next_direction]
                        break
                else:
                    continue


def next_positions(board_in, fish_info):
    idx1, idx2, current_direction = fish_info[0]
    positions = []
    while True:
        idx1 += adj_list[current_direction][0]
        idx2 += adj_list[current_direction][1]
        if 0 <= idx1 < 4 and 0 <= idx2 < 4:
            if board_in[idx1][idx2] == -1:
                continue
            else:
                positions.append((idx1, idx2))
        else:
            return positions


def solution(board_in, fish_info, total):
    global answer

    fish_move(board_in, fish_info)
    positions = next_positions(board_in, fish_info)
    if positions:
        idx1, idx2, direction_shark = fish_info[0]
        for nxt1, nxt2 in positions:
            board_next = copy.deepcopy(board_in)
            fish_info_next = copy.deepcopy(fish_info)

            fish_eaten = board_next[nxt1][nxt2]
            fish_info_next[0] = [nxt1, nxt2, fish_info_next[fish_eaten][2]]
            fish_info_next[fish_eaten] = [-1, -1, -1]
            board_next[idx1][idx2], board_next[nxt1][nxt2] = -1, 0
            solution(board_next, fish_info_next, total+fish_eaten)

    elif total > answer:
        answer = total


board_init = [[0] * 4 for _ in range(4)]
fish_info_init = [[0, 0, 0] for _ in range(17)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        board_init[i][j] = data[2*j]
        fish_info_init[data[2*j]] = [i, j, data[2*j+1]]

number = board_init[0][0]               # number of first fish which is eaten by shark
direction = fish_info_init[number][2]
board_init[0][0] = 0                    # index 0 is for shark
fish_info_init[0] = [0, 0, direction]
fish_info_init[number] = [-1, -1, -1]   # mark eaten

adj_list = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
answer = number
solution(board_init, fish_info_init, number)

print(answer)
