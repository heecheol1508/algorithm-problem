from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]

    man = deque()
    fire = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i, j))
            elif board[i][j] == '@':
                man.append((i, j))

    time = 0
    flag = False
    while man:
        time += 1
        for _ in range(len(fire)):
            idx1, idx2 = fire.popleft()
            for di, dj in adj:
                nxt1, nxt2 = idx1 + di, idx2 + dj
                if 0 <= nxt1 < h and 0 <= nxt2 < w:
                    if board[nxt1][nxt2] == '.' or board[nxt1][nxt2] == '@':
                        board[nxt1][nxt2] = '*'
                        fire.append((nxt1, nxt2))
        for _ in range(len(man)):
            idx1, idx2 = man.popleft()
            for di, dj in adj:
                nxt1, nxt2 = idx1 + di, idx2 + dj
                if 0 <= nxt1 < h and 0 <= nxt2 < w:
                    if board[nxt1][nxt2] == '.':
                        board[nxt1][nxt2] = '@'
                        man.append((nxt1, nxt2))
                else:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        print(time)
    else:
        print('IMPOSSIBLE')
