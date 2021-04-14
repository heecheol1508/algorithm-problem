import sys
sys.stdin = open('input.txt', 'r')


N, K, R = map(int, input().split())
board = [[[True] * 4 for _ in range(N)] for __ in range(N)]
pos_to_idx = {(-1, 0): 0, (0, 1): 1, (1, 0): 2, (0, -1): 3}
idx_to_pos = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    dr1, dc1 = r2 - r1, c2 - c1
    dr2, dc2 = r1 - r2, c1 - c2
    board[r1-1][c1-1][pos_to_idx[(dr1, dc1)]] = False
    board[r2-1][c2-1][pos_to_idx[(dr2, dc2)]] = False

board2 = [[0] * N for _ in range(N)]
color = 0
for i in range(N):
    for j in range(N):
        if board2[i][j] == 0:
            color += 1
            board2[i][j] = color
            queue = [(i, j)]
            while queue:
                idx1, idx2 = queue.pop(0)
                for k in range(4):
                    if board[idx1][idx2][k]:
                        nxt1, nxt2 = idx1 + idx_to_pos[k][0], idx2 + idx_to_pos[k][1]
                        if 0 <= nxt1 < N and 0 <= nxt2 < N and board2[nxt1][nxt2] == 0:
                            board2[nxt1][nxt2] = color
                            queue.append((nxt1, nxt2))

count = [0] * (color+1)
for _ in range(K):
    r, c = map(int, input().split())
    count[board2[r-1][c-1]] += 1

answer = 0
for i in range(1, color):
    if count[i] > 0:
        for j in range(i+1, color+1):
            if count[j] > 0:
                answer += count[i] * count[j]

print(answer)
