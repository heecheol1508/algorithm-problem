import sys
sys.stdin = open('input.txt', 'r')


def to_integer(n):
    if n == 'H':
        return 0
    else:
        return int(n)


def solution(n, idx1, idx2):
    global answer

    if len(board2[idx1][idx2]) == 0:
        answer = max(answer, n)
    else:
        for nxt1, nxt2 in board2[idx1][idx2]:
            if dp[nxt1][nxt2] >= n:
                continue
            else:
                dp[nxt1][nxt2] = n
            if visit[nxt1][nxt2]:
                return False
            visit[nxt1][nxt2] = True
            if solution(n+1, nxt1, nxt2) is False:
                return False
            visit[nxt1][nxt2] = False

    return True


N, M = map(int, input().split())
board = [list(map(to_integer, list(input()))) for _ in range(N)]

board2 = [[[] for _ in range(M)] for __ in range(N)]
for i in range(N):
    for j in range(M):
        d = board[i][j]
        if d > 0:
            ni1, ni2 = i - d, i + d
            nj1, nj2 = j - d, j + d
            if ni1 >= 0 and board[ni1][j] > 0:
                board2[i][j].append((ni1, j))
            if ni2 < N and board[ni2][j] > 0:
                board2[i][j].append((ni2, j))
            if nj1 >= 0 and board[i][nj1] > 0:
                board2[i][j].append((i, nj1))
            if nj2 < M and board[i][nj2] > 0:
                board2[i][j].append((i, nj2))

answer = 0
visit = [[False] * M for _ in range(N)]
visit[0][0] = True
dp = [[0] * M for _ in range(N)]

if solution(1, 0, 0):
    print(answer)
else:
    print(-1)
