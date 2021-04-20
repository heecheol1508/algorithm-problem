import sys
sys.stdin = open('input.txt', 'r')


board = [['#'] * 101 for _ in range(101)]
r = 50
c = 50
d = 0
adj = [(1, 0), (0, -1), (-1, 0), (0, 1)]

N = int(input())
note = list(input())
board[r][c] = '.'
rows = [r]
cols = [c]

for i in range(N):
    if note[i] == 'F':
        r += adj[d][0]
        c += adj[d][1]
        board[r][c] = '.'
        rows.append(r)
        cols.append(c)
    elif note[i] == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

row_max = max(rows)
row_min = min(rows)
col_max = max(cols)
col_min = min(cols)

for i in range(row_min, row_max + 1):
    print(' '.join(board[i][col_min:col_max+1]))
