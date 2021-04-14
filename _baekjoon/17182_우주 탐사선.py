import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        if i == k:
            continue
        for j in range(N):
            if j == i or j == k:
                continue
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

queue = []
heapq.heappush(queue, (0, K, [False]*N))

while queue:
    val, idx, visit = heapq.heappop(queue)
    visit[idx] = True

    flag = True
    for nxt in range(N):
        if visit[nxt] is False:
            heapq.heappush(queue, (val+board[idx][nxt], nxt, visit[:]))
            flag = False
    if flag:
        print(val)
        break
