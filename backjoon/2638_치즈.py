import sys
sys.stdin = open('input.txt', 'r')


def mark_air(mark):
    board[0][0] = mark
    queue = [(0, 0)]
    set_cheese = set()

    while queue:
        idx1, idx2 = queue.pop(0)
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] == 1:
                    set_cheese.add((nxt1, nxt2))
                elif board[nxt1][nxt2] != mark:
                    board[nxt1][nxt2] = mark
                    queue.append((nxt1, nxt2))
    return set_cheese


def melting(set_cheese):
    will_melt = []
    for idx1, idx2 in set_cheese:
        cnt = 0
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] > 1:
                    cnt += 1
                    if cnt == 2:
                        will_melt.append((idx1, idx2))
                        break
    for idx1, idx2 in will_melt:
        board[idx1][idx2] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
hour = 0

while True:
    cheese = mark_air(hour+2)
    if cheese:
        melting(cheese)
    else:
        break
    hour += 1

print(hour)
