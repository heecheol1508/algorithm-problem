import sys
sys.stdin = open('input.txt', 'r')
import itertools


N, M, G, R = map(int, input().split())
board_init = [list(map(int, input().split())) for _ in range(N)]

ground = set()

for i in range(N):
    for j in range(M):
        if board_init[i][j] == 2:
            board_init[i][j] = 1
            ground.add((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

for green in itertools.combinations(ground, G):
    ground_left = ground - set(green)
    for red in itertools.combinations(ground_left, R):
        queue_green = list(green)
        queue_red = list(red)
        board = [row[:] for row in board_init]
        cnt = 0

        n = 2
        for i, j in queue_green:
            board[i][j] = n
        for i, j in queue_red:
            board[i][j] = -n

        while queue_green and queue_red:
            n += 1

            for _ in range(len(queue_green)):
                idx1, idx2 = queue_green.pop(0)
                if board[idx1][idx2] == 0:
                    continue

                for k in range(4):
                    nxt1, nxt2 = idx1 + dx[k], idx2 + dy[k]
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if board[nxt1][nxt2] == 1:
                            board[nxt1][nxt2] = n
                            queue_green.append((nxt1, nxt2))

            for _ in range(len(queue_red)):
                idx1, idx2 = queue_red.pop(0)

                for k in range(4):
                    nxt1, nxt2 = idx1 + dx[k], idx2 + dy[k]
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if board[nxt1][nxt2] == 1:
                            board[nxt1][nxt2] = -n
                            queue_red.append((nxt1, nxt2))
                        elif board[nxt1][nxt2] == n:
                            board[nxt1][nxt2] = 0
                            cnt += 1

        if cnt > answer:
            answer = cnt

print(answer)
