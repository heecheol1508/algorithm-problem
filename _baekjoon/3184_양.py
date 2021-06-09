import collections
import sys
sys.stdin = open('input.txt', 'r')


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

area = {}
index = {'.': 0, 'o': 1, 'v': 2}
for i in range(R):
    for j in range(C):
        if board[i][j] != '#':
            pos = (i, j)
            area[pos] = [0, 0, 0]
            area[pos][index[board[i][j]]] = 1
            board[i][j] = '#'
            queue = collections.deque([pos])
            while queue:
                idx1, idx2 = queue.popleft()
                for di, dj in adj:
                    nxt1, nxt2 = idx1 + di, idx2 + dj
                    if 0 <= nxt1 < R and 0 <= nxt2 < C and board[nxt1][nxt2] != '#':
                        area[pos][index[board[nxt1][nxt2]]] += 1
                        board[nxt1][nxt2] = '#'
                        queue.append((nxt1, nxt2))

sheep = 0
wolves = 0
for [a, b, c] in area.values():
    if b > c:
        sheep += b
    else:
        wolves += c

print(sheep, wolves)
