import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find():
    visit = [[False] * N for _ in range(N)]
    group = []
    index = {}
    for i in range(N):
        for j in range(N):
            if visit[i][j] is False and board[i][j] > 0:
                visit[i][j] = True
                rainbow = []
                general = [(i, j)]
                queue = [(i, j)]
                while queue:
                    ci, cj = queue.pop(0)
                    for di, dj in adj:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] is False:
                            if board[ni][nj] <= -1:
                                visit[ni][nj] = True
                            elif board[ni][nj] == board[i][j]:
                                visit[ni][nj] = True
                                general.append((ni, nj))
                                queue.append((ni, nj))
                            elif board[ni][nj] == 0 and (ni, nj) not in rainbow:
                                rainbow.append((ni, nj))
                                queue.append((ni, nj))
                if len(general) + len(rainbow) >= 2:
                    heapq.heappush(group, (-len(general)-len(rainbow), -len(rainbow), -i, -j))
                    index[(i, j)] = general + rainbow

    if len(group) > 0:
        a, b, c, d = heapq.heappop(group)
        for i, j in index[(-c, -d)]:
            board[i][j] = -2
        return -a
    else:
        return 0


def gravity():
    for j in range(N):
        for i1 in range(N-1, 0, -1):
            if board[i1][j] == -2:
                for i2 in range(i1-1, -1, -1):
                    if board[i2][j] == -1:
                        break
                    elif board[i2][j] >= 0:
                        board[i1][j], board[i2][j] = board[i2][j], board[i1][j]
                        break


def turn_90():
    for i in range(N):
        for j in range(N):
            board[i][j] = board2[j][N-i-1]


answer = 0
while True:
    size = find()
    if size > 0:
        answer += size ** 2
    else:
        break

    gravity()
    board2 = [row[:] for row in board]
    turn_90()
    gravity()

print(answer)
