import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


T = int(input())
adj = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

for _ in range(T):
    N = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if a == c and b == d:
        print(0)
        continue

    board = [[False] * N for _ in range(N)]
    board[a][b] = True
    queue = deque([(a, b)])
    cnt = 0
    flag = False
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            idx1, idx2 = queue.popleft()
            for di, dj in adj:
                nxt1, nxt2 = idx1 + di, idx2 + dj
                if 0 <= nxt1 < N and 0 <= nxt2 < N and board[nxt1][nxt2] is False:
                    board[nxt1][nxt2] = True
                    if nxt1 == c and nxt2 == d:
                        flag = True
                        break
                    queue.append((nxt1, nxt2))
            if flag:
                break
        if flag:
            break
    print(cnt)

