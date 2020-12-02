import sys
sys.stdin = open('input.txt', 'r')

import collections


joint_type = {
    1: ['U', 'R', 'D', 'L'],
    2: ['U', 'D'],
    3: ['R', 'L'],
    4: ['U', 'R'],
    5: ['R', 'D'],
    6: ['D', 'L'],
    7: ['U', 'L']
}

index = {
    'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)
}

next_joint = {
    'U': [1, 2, 5, 6],
    'R': [1, 3, 6, 7],
    'D': [1, 2, 4, 7],
    'L': [1, 3, 4, 5]
}

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    visit[R][C] = True

    queue = collections.deque([(R, C)])
    for __ in range(L-1):
        for _ in range(len(queue)):
            idx1, idx2 = queue.popleft()

            for d in joint_type[board[idx1][idx2]]:
                nxt1, nxt2 = idx1 + index[d][0], idx2 + index[d][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M and visit[nxt1][nxt2] is False:
                    if board[nxt1][nxt2] in next_joint[d]:
                        visit[nxt1][nxt2] = True
                        queue.append((nxt1, nxt2))

    answer = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                answer += 1

    print('#{} {}'.format(t, answer))
