import heapq
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [[0] * N for _ in range(N)]
like = {}
adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(N**2):
    students = list(map(int, input().split()))
    student = students[0]
    like[student] = students[1:]

    temp = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt_like = 0
                cnt_zero = 0
                for di, dj in adj:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if board[ni][nj] == 0:
                            cnt_zero += 1
                        elif board[ni][nj] in like[student]:
                            cnt_like += 1
                heapq.heappush(temp, (-cnt_like, -cnt_zero, i, j))
    a, b, c, d = heapq.heappop(temp)
    board[c][d] = student

result = 0
for i in range(N):
    for j in range(N):
        student = board[i][j]
        cnt = 0
        for di, dj in adj:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] in like[student]:
                cnt += 1
        if cnt > 0:
            result += 10 ** (cnt - 1)

print(result)
