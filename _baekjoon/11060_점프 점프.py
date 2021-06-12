import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
maze = list(map(int, input().split()))

visit = [N] * N
visit[0] = 0

queue = [0]
while queue:
    cur = queue.pop(0)
    if cur == N - 1:
        break

    cnt_jump = visit[cur] + 1
    for nxt in range(min(cur+maze[cur], N-1), cur, -1):
        if visit[nxt] <= cnt_jump:
            break
        else:
            visit[nxt] = cnt_jump
            queue.append(nxt)

if visit[-1] == N:
    print(-1)
else:
    print(visit[-1])
