import sys
sys.stdin = open('input.txt', 'r')


def finger_next(idx1, idx2, d):
    left1, left2 = idx1 + near_by_direction[d-1][0], idx2 + near_by_direction[d-1][1]
    if visit[left1][left2] is False:
        return left1, left2, (d-1) % 4
    else:
        nxt1, nxt2 = idx1 + near_by_direction[d][0], idx2 + near_by_direction[d][1]
        return nxt1, nxt2, d


def actual_move(idx1, idx2, d):
    global total_out

    sand_left = board[idx1][idx2]
    for val, adj_list in sand_moved[d].items():
        sand = int(board[idx1][idx2] * val)
        if sand > 0:
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                sand_left -= sand
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    board[nxt1][nxt2] += sand
                else:
                    total_out += sand

    nxt1, nxt2 = idx1 + near_by_direction[d][0], idx2 + near_by_direction[d][1]
    if 0 <= nxt1 < N and 0 <= nxt2 < N:
        board[nxt1][nxt2] += sand_left
    else:
        total_out += sand_left
    board[idx1][idx2] = 0


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

near_by_direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [[False] * N for _ in range(N)]

sand_moved = {
    0: {
        0.01: [(1, -1), (1, 1)],
        0.02: [(0, -2), (0, 2)],
        0.05: [(-2, 0)],
        0.07: [(0, -1), (0, 1)],
        0.10: [(-1, -1), (-1, 1)]
    },
    1: {
        0.01: [(-1, -1), (1, -1)],
        0.02: [(-2, 0), (2, 0)],
        0.05: [(0, 2)],
        0.07: [(-1, 0), (1, 0)],
        0.10: [(-1, 1), (1, 1)]
    },
    2: {
        0.01: [(-1, -1), (-1, 1)],
        0.02: [(0, -2), (0, 2)],
        0.05: [(2, 0)],
        0.07: [(0, -1), (0, 1)],
        0.10: [(1, -1), (1, 1)]
    },
    3: {
        0.01: [(-1, 1), (1, 1)],
        0.02: [(-2, 0), (2, 0)],
        0.05: [(0, -2)],
        0.07: [(-1, 0), (1, 0)],
        0.10: [(-1, -1), (1, -1)]
    }
}

c1 = c2 = N // 2
cd = 0
total_out = 0

while True:
    visit[c1][c2] = True
    n1, n2, nd = finger_next(c1, c2, cd)
    actual_move(n1, n2, nd)
    if n1 == 0 and n2 == 0:
        break
    else:
        c1, c2, cd = n1, n2, nd

print(total_out)
