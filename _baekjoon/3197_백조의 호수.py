from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px, py = find(x), find(y)
    if px > py:
        parent[px] = py
        find(x)
    elif px < py:
        parent[py] = px
        find(y)


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

swan = []
lake = []

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            N += 1
            board[i][j] = N
            lake.append((i, j))
            queue = deque([(i, j)])
            while queue:
                idx1, idx2 = queue.popleft()
                for di, dj in adj:
                    nxt1, nxt2 = idx1 + di, idx2 + dj
                    if 0 <= nxt1 < R and 0 <= nxt2 < C:
                        if board[nxt1][nxt2] == '.':
                            board[nxt1][nxt2] = N
                            lake.append((nxt1, nxt2))
                            queue.append((nxt1, nxt2))
                        elif board[nxt1][nxt2] == 'L':
                            swan.append(N)
                            board[nxt1][nxt2] = N
                            lake.append((nxt1, nxt2))
                            queue.append((nxt1, nxt2))
        elif board[i][j] == 'L':
            N += 1
            swan.append(N)
            board[i][j] = N
            lake.append((i, j))
            queue = deque([(i, j)])
            while queue:
                idx1, idx2 = queue.popleft()
                for di, dj in adj:
                    nxt1, nxt2 = idx1 + di, idx2 + dj
                    if 0 <= nxt1 < R and 0 <= nxt2 < C:
                        if board[nxt1][nxt2] == '.':
                            board[nxt1][nxt2] = N
                            lake.append((nxt1, nxt2))
                            queue.append((nxt1, nxt2))

parent = list(range(N+1))
days = 0

while find(swan[0]) != find(swan[1]):
    days += 1
    melt = []
    for i in range(len(lake)):
        idx1, idx2 = lake[i]
        for di, dj in adj:
            nxt1, nxt2 = idx1 + di, idx2 + dj
            if 0 <= nxt1 < R and 0 <= nxt2 < C and board[nxt1][nxt2] == 'X':
                board[nxt1][nxt2] = '.'
                melt.append((nxt1, nxt2))

    lake = []
    for i in range(len(melt)):
        idx1, idx2 = melt[i]
        numbers = set()
        for di, dj in adj:
            nxt1, nxt2 = idx1 + di, idx2 + dj
            if 0 <= nxt1 < R and 0 <= nxt2 < C and board[nxt1][nxt2] != 'X' and board[nxt1][nxt2] != '.':
                numbers.add(find(board[nxt1][nxt2]))
        if len(numbers) == 1:
            board[idx1][idx2] = numbers.pop()
            lake.append((idx1, idx2))
        else:
            a = numbers.pop()
            for b in numbers:
                union(a, b)
            board[idx1][idx2] = find(a)
            lake.append((idx1, idx2))

print(days)
