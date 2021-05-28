import sys
sys.stdin = open('input.txt', 'r')


def indexing(n2):
    adj1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i, j, d1 = 0, 0, 0
    for n in range(n2, 0, -1):
        index[i][j] = n
        ni, nj = i + adj1[d1][0], j + adj1[d1][1]
        if 0 <= ni < N and 0 <= nj < N and index[ni][nj] == 0:
            i, j = ni, nj
        else:
            d1 = (d1 + 1) % 4
            i, j = i + adj1[d1][0], j + adj1[d1][1]


def balls_init():
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                balls[index[i][j]] = board[i][j]


def shorten():
    for i in range(1, N**2-1):
        if balls[i] == 0:
            for j in range(i+1, N**2):
                if balls[j] != 0:
                    balls[i], balls[j] = balls[j], balls[i]
                    break


def explode():
    exploded = 0
    cnt = 0
    for i in range(1, N**2):
        if balls[i] == 0:
            if cnt >= 4:
                exploded += balls[i-1] * cnt
                for j in range(i-cnt, i):
                    balls[j] = 0
            break
        if balls[i] == balls[i-1]:
            cnt += 1
        elif cnt >= 4:
            exploded += balls[i-1] * cnt
            for j in range(i-cnt, i):
                balls[j] = 0
            cnt = 1
        else:
            cnt = 1
    else:
        if cnt >= 4:
            exploded += balls[-1] * cnt
            for j in range(1, cnt+1):
                balls[-j] = 0
    return exploded


def lengthen():
    new_balls = [0]
    cnt = 1

    for i in range(2, N**2):
        if balls[i] == balls[i-1]:
            cnt += 1
        else:
            new_balls.append(cnt)
            new_balls.append(balls[i-1])
            if balls[i] == 0:
                break
            else:
                cnt = 1

    if len(new_balls) < N**2:
        zero = [0] * (N**2 - len(new_balls))
        return new_balls + zero
    else:
        return new_balls[:N**2]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

index = [[0] * N for _ in range(N)]
indexing(N**2 - 1)

balls = [0] * N**2
balls_init()

adj = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
ci, cj = N // 2, N // 2

answer = 0
for _ in range(M):
    d, s = map(int, input().split())
    for k in range(1, s+1):
        balls[index[ci + adj[d][0] * k][cj + adj[d][1] * k]] = 0

    shorten()

    while True:
        tmp = explode()
        if tmp > 0:
            answer += tmp
            shorten()
        else:
            break

    if balls[1] == 0:
        break
    else:
        balls = lengthen()

print(answer)
