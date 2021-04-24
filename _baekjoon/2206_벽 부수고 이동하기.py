import collections
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

inf = float('inf')
dp = [[[inf, inf] for _ in range(M)] for _ in range(N)]
dp[0][0][0] = 1

queue = collections.deque([(0, 0, 1, False)])
adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while queue:
    idx1, idx2, cnt, broken = queue.popleft()
    cnt += 1

    if broken:
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M and board[nxt1][nxt2] == '0':
                if cnt >= dp[nxt1][nxt2][0]:
                    continue
                elif cnt < dp[nxt1][nxt2][1]:
                    dp[nxt1][nxt2][1] = cnt
                    queue.append((nxt1, nxt2, cnt, True))
    else:
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] == '1':
                    if cnt < dp[nxt1][nxt2][1]:
                        dp[nxt1][nxt2][1] = cnt
                        queue.append((nxt1, nxt2, cnt, True))
                else:
                    if cnt < dp[nxt1][nxt2][0]:
                        dp[nxt1][nxt2][0] = cnt
                        queue.append((nxt1, nxt2, cnt, False))

if min(dp[-1][-1]) == inf:
    print(-1)
else:
    print(min(dp[-1][-1]))