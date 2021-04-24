import collections
import sys
sys.stdin = open('input.txt', 'r')


def n_step(n, board1):
    global answer

    cnt = 0
    for j in range(W):
        for i in range(H-1, -1, -1):
            if board1[i][j]:
                cnt += 1
            else:
                break

    answer = min(answer, cnt)

    if n == N:
        return

    else:
        for j in range(W):
            for i in range(H):
                if board1[i][j] != 0:
                    break
            else:
                continue

            board2 = [row[:] for row in board1]
            if board2[i][j] == 1:
                board2[i][j] = 0
                n_step(n + 1, [row[:] for row in board2])
            else:
                queue = collections.deque([(i, j, board2[i][j])])
                board2[i][j] = 0
                while queue:
                    idx1, idx2, power = queue.popleft()
                    for k in range(1, power):
                        for adj in adj_list:
                            nxt1, nxt2 = idx1 + adj[0] * k, idx2 + adj[1] * k
                            if 0 <= nxt1 < H and 0 <= nxt2 < W:
                                if board2[nxt1][nxt2] > 1:
                                    queue.append((nxt1, nxt2, board2[nxt1][nxt2]))
                                    board2[nxt1][nxt2] = 0
                                elif board2[nxt1][nxt2] == 1:
                                    board2[nxt1][nxt2] = 0

                for c in range(W):
                    for r1 in range(H-1, 0, -1):
                        if board2[r1][c] == 0:
                            for r2 in range(r1-1, -1, -1):
                                if board2[r2][c] != 0:
                                    board2[r1][c], board2[r2][c] = board2[r2][c], board2[r1][c]
                                    break

                n_step(n + 1, [row[:] for row in board2])

    return


T = int(input())
adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for t in range(1, T+1):
    N, W, H = map(int, input().split())
    board0 = [list(map(int, input().split())) for _ in range(H)]

    answer = 0
    for i0 in range(H):
        for j0 in range(W):
            if board0[i0][j0]:
                answer += 1

    n_step(0, [row[:] for row in board0])
    print('#{} {}'.format(t, answer))
