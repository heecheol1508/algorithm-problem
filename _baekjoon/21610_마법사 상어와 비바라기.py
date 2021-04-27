import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj1 = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
adj2 = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    di, dj = adj1[d][0] * s, adj1[d][1] * s

    cloud_moved = []
    for _ in range(len(cloud)):
        ci, cj = cloud.pop()
        ni, nj = (ci + di) % N, (cj + dj) % N
        cloud_moved.append((ni, nj))

    rained = [[False] * N for _ in range(N)]
    for i, j in cloud_moved:
        board[i][j] += 1
        rained[i][j] = True

    for i, j in cloud_moved:
        cnt = 0
        for k in range(4):
            ni, nj = i + adj2[k][0], j + adj2[k][1]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] > 0:
                cnt += 1
        board[i][j] += cnt

    for i in range(N):
        for j in range(N):
            if rained[i][j] is False and board[i][j] >= 2:
                board[i][j] -= 2
                cloud.append((i, j))

answer = 0
for r in range(N):
    answer += sum(board[r])

print(answer)
