import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


N, Q = map(int, input().split())
board = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    board[p].append((q, r))
    board[q].append((p, r))

answer = []
for _ in range(Q):
    k, v = map(int, input().split())

    cnt = 0
    queue = [(0, v)]
    while queue:
        i, j = queue.pop(0)
        for v, d in board[j]:
            if v == i or d < k:
                continue
            else:
                queue.append((j, v))
                cnt += 1
    answer.append(str(cnt))

print('\n'.join(answer))
