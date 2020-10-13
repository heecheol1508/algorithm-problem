import sys
sys.stdin = open('input.txt', 'r')


# set conditions
N, M, k = map(int, input().split())
board_shark = [list(map(int, input().split())) for _ in range(N)]

direction_init = [0] + list(map(int, input().split()))

direction_info = {}
for num in range(1, M+1):
    direction_info[num] = {}
    for di in range(1, 5):
        direction_info[num][di] = list(map(int, input().split()))

adj_list = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
board_smell = [[(0, 0)] * N for _ in range(N)]

current_shark_info = {}
for i in range(N):
    for j in range(N):
        if board_shark[i][j] > 0:
            current_shark_info[board_shark[i][j]] = (i, j, direction_init[board_shark[i][j]])
            board_smell[i][j] = (board_shark[i][j], k)

# process
time = 0
while len(current_shark_info) > 1:
    if time >= 1000:
        time = -1
        break
    time += 1
    for number, (idx1, idx2, d) in sorted(current_shark_info.items()):
        # print(number)
        for nd in direction_info[number][d]:
            nxt1, nxt2 = idx1 + adj_list[nd][0], idx2 + adj_list[nd][1]
            if 0 <= nxt1 < N and 0 <= nxt2 < N and board_smell[nxt1][nxt2] == (0, 0):
                if board_shark[nxt1][nxt2] == 0 or board_shark[nxt1][nxt2] > number:
                    board_shark[nxt1][nxt2] = number
                    current_shark_info[number] = (nxt1, nxt2, nd)
                else:
                    del(current_shark_info[number])
                if board_shark[idx1][idx2] == number:
                    board_shark[idx1][idx2] = 0
                break
        else:
            for nd in direction_info[number][d]:
                nxt1, nxt2 = idx1 + adj_list[nd][0], idx2 + adj_list[nd][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N and board_smell[nxt1][nxt2][0] == number:
                    if board_shark[nxt1][nxt2] == 0 or board_shark[nxt1][nxt2] > number:
                        board_shark[nxt1][nxt2] = number
                        current_shark_info[number] = (nxt1, nxt2, nd)
                    else:
                        del(current_shark_info[number])
                    if board_shark[idx1][idx2] == number:
                        board_shark[idx1][idx2] = 0
                    break

    for i in range(N):
        for j in range(N):
            if board_shark[i][j] != 0:
                board_smell[i][j] = (board_shark[i][j], k)
                continue
            elif board_smell[i][j][0] == 0:
                continue
            elif board_smell[i][j][1] == 1:
                board_smell[i][j] = (0, 0)
            else:
                board_smell[i][j] = (board_smell[i][j][0], board_smell[i][j][1]-1)

    # print(current_shark_info)
    # print()
    # for i in range(N):
    #     print(board_shark[i], board_smell[i])
    # print()
    # print()

print(time)
