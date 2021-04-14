import sys
sys.stdin = open('input.txt', 'r')


def binary(s):
    return format(int(s), '04b')


N, M = map(int, input().split())
board = [list(map(binary, input().split())) for _ in range(M)]
color = [[0] * N for _ in range(M)]
c = 0
adj_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(M):
    for j in range(N):
        if color[i][j] == 0:
            c += 1
            color[i][j] = c
            queue = [(i, j)]
            while queue:
                idx1, idx2 = queue.pop(0)
                for k in range(4):
                    if board[idx1][idx2][k] == '0':
                        nxt1, nxt2 = idx1 + adj_list[k][0], idx2 + adj_list[k][1]
                        if color[nxt1][nxt2] == 0:
                            color[nxt1][nxt2] = c
                            queue.append((nxt1, nxt2))

print(c)
count = {}
for i in range(1, c+1):
    count[i] = 0

close = set()
for i in range(M):
    for j in range(N):
        count[color[i][j]] += 1
        if i < M - 1 and color[i][j] != color[i+1][j]:
            close.add((color[i][j], color[i+1][j]))
        if j < N - 1 and color[i][j] != color[i][j+1]:
            close.add((color[i][j], color[i][j+1]))

print(max(count.values()))

answer = 0
for _ in range(len(close)):
    a, b = close.pop()
    answer = max(answer, count[a] + count[b])

print(answer)
