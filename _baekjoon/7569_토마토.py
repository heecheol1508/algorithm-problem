from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


M, N, H = map(int, input().split())
box = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    box.append(layer)

red = deque()
flag = True
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                red.append((h, i, j))
            elif flag and box[h][i][j] == 0:
                flag = False

if flag:
    print(0)
else:
    adj = [(-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0)]
    days = 0
    while red:
        days += 1
        for _ in range(len(red)):
            h, i, j = red.popleft()
            for k in range(6):
                nh, ni, nj = h + adj[k][0], i + adj[k][1], j + adj[k][2]
                if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and box[nh][ni][nj] == 0:
                    box[nh][ni][nj] = days
                    red.append((nh, ni, nj))

    answer = 1
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] > answer:
                    answer = box[h][i][j]
                elif box[h][i][j] == 0:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        print(-1)
    else:
        print(answer)
