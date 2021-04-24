import sys
sys.stdin = open('input.txt', 'r')


adj_list = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [input().split() for _ in range(h)]
    mark = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '1':
                mark += 1
                board[i][j] = mark
                queue = [(i, j)]
                while queue:
                    idx1, idx2 = queue.pop(0)
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < h and 0 <= nxt2 < w and board[nxt1][nxt2] == '1':
                            board[nxt1][nxt2] = mark
                            queue.append((nxt1, nxt2))

    print(mark)

