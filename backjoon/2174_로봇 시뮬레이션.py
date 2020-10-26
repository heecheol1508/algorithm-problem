import sys
sys.stdin = open('input.txt', 'r')


A, B = map(int, input().split())
board = [[0] * A for _ in range(B)]

N, M = map(int, input().split())
robot_info = {}
for i in range(1, N+1):
    info = input().split()
    x = int(info[0]) - 1
    y = int(info[1]) - 1
    robot_info[i] = [y, x, info[2]]
    board[y][x] = i

direction_info = {
    'N': ['W', 'E', (1, 0)],
    'W': ['S', 'N', (0, -1)],
    'S': ['E', 'W', (-1, 0)],
    'E': ['N', 'S', (0, 1)]
}

flag = False
for _ in range(M):
    command = input().split()
    num_robot, command_type, repeat = int(command[0]), command[1], int(command[2])

    if command_type == 'L':
        for _ in range(repeat % 4):
            robot_info[num_robot][2] = direction_info[robot_info[num_robot][2]][0]
    elif command_type == 'R':
        for _ in range(repeat % 4):
            robot_info[num_robot][2] = direction_info[robot_info[num_robot][2]][1]
    else:
        adj1, adj2 = direction_info[robot_info[num_robot][2]][2]
        idx1, idx2 = robot_info[num_robot][0], robot_info[num_robot][1]
        for k in range(1, repeat+1):
            nxt1, nxt2 = idx1 + k*adj1, idx2 + k*adj2
            if 0 <= nxt1 < B and 0 <= nxt2 < A:
                if board[nxt1][nxt2] > 0:
                    print('Robot', num_robot, 'crashes into robot', board[nxt1][nxt2])
                    flag = True
                    break
            else:
                print('Robot', num_robot, 'crashes into the wall')
                flag = True
                break
        if flag:
            break
        else:
            nxt1, nxt2 = idx1 + repeat*adj1, idx2 + repeat*adj2
            board[nxt1][nxt2], board[idx1][idx2] = num_robot, 0
            robot_info[num_robot][0], robot_info[num_robot][1] = nxt1, nxt2

else:
    print('OK')
