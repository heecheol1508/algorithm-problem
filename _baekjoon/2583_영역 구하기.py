# 13:53 ~ 14:07
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            board[i][j] = 1

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = []

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            board[i][j] = 1
            cnt = 1
            queue = deque([(i, j)])
            while queue:
                idx1, idx2 = queue.popleft()
                for di, dj in adj:
                    nxt1, nxt2 = idx1 + di, idx2 + dj
                    if 0 <= nxt1 < M and 0 <= nxt2 < N and board[nxt1][nxt2] == 0:
                        board[nxt1][nxt2] = 1
                        cnt += 1
                        queue.append((nxt1, nxt2))
            answer.append(cnt)

print(len(answer))
print(' '.join(map(str, sorted(answer))))
