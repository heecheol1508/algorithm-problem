import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline().rstrip()


R, C = map(int, input().split())
inf = float('inf')
board = [[inf] * C] + [list(map(int, input().split())) for _ in range(R)]   # 1행 추가

visit = [[0] * C for _ in range(R+1)]
visit[0][0] = 1

queue = [(1, 0)]
adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while queue:
    idx1, idx2 = queue.pop(0)
    if (idx1, idx2) in queue:
        continue
    cnt = 0
    for adj in adj_list:
        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
        if 0 <= nxt1 < R+1 and 0 <= nxt2 < C:
            if board[nxt1][nxt2] > board[idx1][idx2]:
                cnt += visit[nxt1][nxt2]
            elif board[nxt1][nxt2] < board[idx1][idx2]:
                queue.append((nxt1, nxt2))
    visit[idx1][idx2] = cnt

print(visit[R][C-1])
