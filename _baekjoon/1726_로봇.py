import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int,  input().split())
board = [input().split() for _ in range(N)]

adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
new_d = [0, 0, 2, 1, 3]

a, b, c = map(int, input().split())
i, j, d = a - 1, b - 1, new_d[c]

a, b, c = map(int, input().split())
ti, tj, td = a - 1, b - 1, new_d[c]

visit = [[[False] * 4 for _ in range(M)] for __ in range(N)]
visit[i][j][d] = True

queue = [(i, j, d)]
flag = True
count = 0

while flag:
    for _ in range(len(queue)):
        i, j, d = queue.pop(0)
        if i == ti and j == tj and d == td:
            flag = False
            break

        for k in range(1, 4):
            ni, nj = i + adj[d][0] * k, j + adj[d][1] * k
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == '0':
                if visit[ni][nj][d] is False:
                    visit[ni][nj][d] = True
                    queue.append((ni, nj, d))
            else:
                break

        dr = (d + 1) % 4
        dl = (d - 1) % 4
        if visit[i][j][dr] is False:
            visit[i][j][dr] = True
            queue.append((i, j, dr))
        if visit[i][j][dl] is False:
            visit[i][j][dl] = True
            queue.append((i, j, dl))
    else:
        count += 1

print(count)
