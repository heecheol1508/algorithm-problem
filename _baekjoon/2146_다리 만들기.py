import collections
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [input().split() for _ in range(N)]
mark = {}
adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            n += 1
            board[i][j] = n
            mark[n] = [(i, j)]
            queue = collections.deque([(i, j)])
            while queue:
                idx1, idx2 = queue.popleft()
                for k in range(4):
                    nxt1, nxt2 = idx1 + adj[k][0], idx2 + adj[k][1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < N and board[nxt1][nxt2] == '1':
                        mark[n].append((nxt1, nxt2))
                        board[nxt1][nxt2] = n
                        queue.append((nxt1, nxt2))
        elif board[i][j] == '0':
            board[i][j] = 0

answer = 200
for i in range(1, n+1):
    temp = [row[:] for row in board]
    cnt = 0
    flag = False
    queue = collections.deque(mark[i][:])
    while cnt < answer:
        cnt += 1
        for _ in range(len(queue)):
            idx1, idx2 = queue.popleft()
            for k in range(4):
                nxt1, nxt2 = idx1 + adj[k][0], idx2 + adj[k][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if temp[nxt1][nxt2] == 0:
                        temp[nxt1][nxt2] = i
                        queue.append((nxt1, nxt2))
                    elif temp[nxt1][nxt2] != i:
                        answer = cnt - 1
                        flag = True
                        break
            if flag:
                break
print(answer)
