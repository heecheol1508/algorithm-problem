import sys
sys.stdin = open('input.txt', 'r')


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def throw_the_stick(h, d):
    if d == 1:
        for c in range(C):
            if board[h][c] == 'x':
                board[h][c] = '.'
                return c
    else:
        for c in range(C-1, -1, -1):
            if board[h][c] == 'x':
                board[h][c] = '.'
                return c
    return -1


def clustering(h, c):
    near = []

    for m in range(4):
        nh, nc = h + adj_list[m][0], c + adj_list[m][1]
        if 0 <= nh < R and 0 <= nc < C and board[nh][nc] == 'x':
            board[nh][nc] = m
            mineral = [(nh, nc)]
            idx = 0
            while idx < len(mineral):
                idx1, idx2 = mineral[idx]
                idx += 1
                for adj in adj_list:
                    nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                    if 0 <= nxt1 < R and 0 <= nxt2 < C and board[nxt1][nxt2] == 'x':
                        board[nxt1][nxt2] = m
                        mineral.append((nxt1, nxt2))
            mineral.sort(reverse=True)
            near.append(mineral)

    order = []
    for k in range(len(near)):
        a, b = near[k][0]
        order.append((a, b, k))
    order.sort(reverse=True)

    for a, b, c in order:
        m = board[a][b]
        flag = False
        for dx in range(1, R+1):
            for x, y in near[c]:
                nx = x + dx
                if 0 <= nx < R and (board[nx][y] == '.' or board[nx][y] == m):
                    continue
                else:
                    flag = True
                    break
            if flag:
                break

        if dx == 1:
            for x, y in near[c]:
                board[x][y] = 'x'
        else:
            dx -= 1
            for x, y in near[c]:
                nx = x + dx
                board[nx][y], board[x][y] = 'x', '.'


N = int(input())
height_info = list(map(int, input().split()))

direction = -1
for n in range(N):
    height = R-height_info[n]
    direction *= -1
    column = throw_the_stick(height, direction)
    if column == -1:
        continue
    else:
        clustering(height, column)


for row in board:
    print(''.join(row))

